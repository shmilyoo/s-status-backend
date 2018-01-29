from flask import Flask
from threading import Lock
from app.sio.system_utils import get_server_status
import time
from app import common, config
from app.models import db, socket_session_commit
from app.models.interface_rate import History
from app.config import backendSendInterval
from app.sio import socketIO

thread = None
thread_lock = Lock()
client_number = 0


def create_app(config_file, async_mode):
    app = Flask(__name__)
    app.config.from_object(config_file)

    from app.models import db
    db.init_app(app)

    from app.sio import socketIO, init_sockets
    init_sockets()
    socketIO.init_app(app, async_mode=async_mode)

    from app.api import init_api
    init_api(app)

    run_backend_thread(app, socketIO)
    return app


def run_backend_thread(app, socketIO):
    global thread
    with thread_lock:
        if thread is None:
            thread = socketIO.start_background_task(target=background_thread, app=app)
            print('back task started')


def background_thread(app):
    """
    后台线程，如果有人访问页面，每*秒通过socketio广播一个数组[ss用户数，cpu占用，内存占用，进流量，出流量]
    :return:
    """
    print('start backend send')
    while True:
        status = get_server_status()
        online = sum(status[-1].values())
        with app.app_context():
            store_history(online, *status[1:-1], config.INTERFACE_NAME)
        socketIO.emit('backendSend', status, broadcast=True)
        time.sleep(backendSendInterval)


def store_history(online, cpu, memory, in_speed, out_speed, interface):
    row = History(online, cpu, memory, in_speed, out_speed, interface)
    db.session.add(row)
    return socket_session_commit()

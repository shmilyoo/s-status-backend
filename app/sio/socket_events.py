from datetime import datetime, timezone

from app.sio import socketIO
from threading import Lock
from app.sio.system_utils import get_cpu_percent, get_mem_percent, get_in_speed, get_out_speed, get_ss_client
import time

thread = None
thread_lock = Lock()
client_number = 0  # socketio 的client数量


def init_socket_events():
    print('init socket events')

    @socketIO.on('connect')
    def connect():
        global client_number
        client_number += 1
        print('connected: ' + str(client_number))
        global thread
        with thread_lock:
            if thread is None:
                thread = socketIO.start_background_task(target=background_thread)
                print('back task started')

    @socketIO.on('disconnect')
    def disconnect():
        global client_number
        client_number -= 1
        print('disconnected: ' + str(client_number))


def background_thread():
    """
    后台线程，如果有人访问页面，每2秒通过socketio广播一个数组[ss用户数，cpu占用，内存占用，进流量，出流量]
    :return:
    """
    print('start backend send')
    while True:
        print('back number' + str(client_number))
        if client_number:
            socketIO.emit('backendSend',
                          [datetime.utcnow().replace(tzinfo=timezone.utc).timestamp(), get_cpu_percent(),
                           get_mem_percent(), get_in_speed(), get_out_speed(), get_ss_client()],
                          broadcast=True)
        time.sleep(3)

from app.sio import socketIO
from flask_socketio import emit
from app import get_server_status


def init_socket_events():
    print('init socket events')

    @socketIO.on('connect')
    def connect():
        emit('backendSend',get_server_status())

    @socketIO.on('disconnect')
    def disconnect():
        pass

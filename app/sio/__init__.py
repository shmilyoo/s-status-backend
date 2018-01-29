from flask_socketio import SocketIO

socketIO = SocketIO()
# client_number = 0  # socketio 的client数量


def init_sockets():
    from app.sio.socket_events import init_socket_events
    init_socket_events()

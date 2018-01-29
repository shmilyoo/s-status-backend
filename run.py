"""
循环向socketio客户端发送当前cpu、内存百分比，上下行流量速率
提供CPU内存占比、上下行速率的历史查询
"""
from app import create_app
from app.sio import socketIO

app = create_app('app.config', 'gevent')

if __name__ == '__main__':
    socketIO.run(app, host=app.config['HOST'],
                 port=app.config['PORT'],
                 debug=app.config['DEBUG'])

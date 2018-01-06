from flask import Flask, g


def create_app(config_file, async_mode):
    # print(__name__)
    app = Flask(__name__)
    app.config.from_object(config_file)

    from app.models import db
    db.init_app(app)

    from app.sio import socketIO, init_sockets
    init_sockets()
    socketIO.init_app(app, async_mode=async_mode)

    @app.before_first_request
    def fdf():
        print('first request')

    @app.before_request
    def dfdf():
        print('before request')

    @app.route('/')
    def index():
        g.aa = 'fffdfd'
        return g.get('aaa', 'cccc')

    @app.teardown_request
    def fdf(e):
        # print('teardown')
        pass

    return app

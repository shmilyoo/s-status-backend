from app.models import db
from datetime import datetime


class SpeedRate(db.Model):
    __tablename__ = 'speed_rate'
    id = db.Column(db.Integer, primary_key=True)
    interface = db.Column(db.String(64), nullable=False)  # , comment='流量所在网卡名称'
    rate = db.Column(db.Integer, nullable=False)  # , comment='接口速率'
    is_inbound = db.Column(db.Boolean, default=True, nullable=False)  # , comment='是否是入口流量，出口为false'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)


class Online(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.SmallInteger, nullable=False)  # , comment='在线用户数'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)


class Cpu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    percent = db.Column(db.SmallInteger, nullable=False)  # , comment='cpu总占用百分比，去掉%，取值0-100'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)


class Memory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    percent = db.Column(db.SmallInteger, nullable=False)  # , comment='内存总占用百分比，去掉%，取值0-100'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

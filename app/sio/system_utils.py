import psutil

from app import common
from app.config import INTERFACE_NAME, PROVINCE, geoDbPath, grepStr
from datetime import datetime
import os
import geoip2.database

bytes_sent = 0
bytes_recv = 0
bytes_sent_time = bytes_recv_time = datetime.utcnow()


def get_server_status():
    utcnow_timestamp = common.get_timestamp_utcnow()
    cpu_percent = get_cpu_percent()
    memory_percent = get_memory_percent()
    in_speed = get_in_speed()
    out_speed = get_out_speed()
    ss_client = get_ss_client()
    return [utcnow_timestamp, cpu_percent, memory_percent, in_speed, out_speed, ss_client]


def get_cpu_percent():
    """
    :return: cpu占用百分比 0-100
    """
    return round(psutil.cpu_percent())


def get_memory_percent():
    """
    :return: 内存占用百分比数值，0-100
    """
    return round(psutil.virtual_memory().percent)


def get_out_speed():
    """
    :return: 返回指定接口的出口流量,单位Kb
    """
    _bytes_sent = psutil.net_io_counters(pernic=True)[INTERFACE_NAME].bytes_sent
    global bytes_sent, bytes_sent_time
    spent_seconds = (datetime.utcnow() - bytes_sent_time).total_seconds()
    if bytes_sent == 0:
        result = 0
    else:
        result = round((_bytes_sent - bytes_sent) * 8 / (1024 * spent_seconds))
    bytes_sent = _bytes_sent
    bytes_sent_time = datetime.utcnow()
    return result if result >= 0 else 0


def get_in_speed():
    """
    :return: 返回指定接口的入口流量,单位Kb
    """
    _bytes_recv = psutil.net_io_counters(pernic=True)[INTERFACE_NAME].bytes_recv
    global bytes_recv, bytes_recv_time
    spent_seconds = (datetime.utcnow() - bytes_recv_time).total_seconds()
    if bytes_recv == 0:
        result = 0
    else:
        result = round((_bytes_recv - bytes_recv) * 8 / (1024 * spent_seconds))
    bytes_recv = _bytes_recv
    bytes_recv_time = datetime.utcnow()
    return result if result >= 0 else 0


def get_ss_client():
    """
    ss -atn |grep "162.243.136.175:80" |awk "{print $5}" |cut -d ":" -f1 |sort |uniq
    :return: 连接到ss服务器的用户数目
    """
    # ls = ['49.80.205.41', '202.109.211.200', '117.136.19.125', '111.194.48.201', '218.5.157.116', '49.80.171.144',
    #       '223.85.218.204', '202.109.211.201', '49.80.206.41', '49.80.215.41']
    # import random
    # random.shuffle(ls)
    # ls = ls[0:random.randint(3, 10)]

    result = {}
    reader = geoip2.database.Reader(geoDbPath)

    ips = os.popen(grepStr).readlines()
    # ips = ls
    for ip in ips:
        try:
            response = reader.city(ip)
            province = PROVINCE.get(response.subdivisions.most_specific.name.lower(), '')
            if province:
                result[province] = result.get(province, 0) + 1
        except:
            pass
    reader.close()
    return result

from flask import request, jsonify
from app.models.interface_rate import History


def init_api(app):
    num_per_request = 17280  # 17280*5   为一天的总秒数，配置为一次请求最多获取一天的数据,与后台中的配置保持一致

    @app.route('/api/history')
    def history_index():
        pass

    @app.route('/api/history/online', methods=['get'])
    def history_online():
        start, end, correct, message = check_utc_timestamp()
        if not correct:
            return jsonify({'success': False, 'message': message})
        record = History.query.with_entities(History.online, History.timestamp).filter(History.timestamp >= start,
                                                                                       History.timestamp <= end).limit(
            num_per_request)
        return jsonify(
            {'success': True,
             'data': [{'timestamp': history.timestamp, 'online': history.online} for history in record]})

    @app.route('/api/history/cpu', methods=['get'])
    def history_cpu():
        start, end, correct, message = check_utc_timestamp()
        if not correct:
            return jsonify({'success': False, 'message': message})
        record = History.query.with_entities(History.cpu, History.timestamp).filter(History.timestamp >= start,
                                                                                    History.timestamp <= end).limit(
            num_per_request)
        return jsonify(
            {'success': True, 'data': [{'timestamp': history.timestamp, 'cpu': history.cpu} for history in record]})

    @app.route('/api/history/memory', methods=['get'])
    def history_memory():
        start, end, correct, message = check_utc_timestamp()
        if not correct:
            return jsonify({'success': False, 'message': message})
        record = History.query.with_entities(History.memory, History.timestamp).filter(History.timestamp >= start,
                                                                                       History.timestamp <= end).limit(
            num_per_request)
        return jsonify(
            {'success': True,
             'data': [{'timestamp': history.timestamp, 'memory': history.memory} for history in record]})

    @app.route('/api/history/flow', methods=['get'])
    def history_flow():
        start, end, correct, message = check_utc_timestamp()
        if not correct:
            return jsonify({'success': False, 'message': message})
        record = History.query.with_entities(History.in_speed, History.out_speed, History.timestamp).filter(
            History.timestamp >= start,
            History.timestamp <= end).limit(
            num_per_request)
        return jsonify(
            {'success': True,
             'data': [{'timestamp': history.timestamp, 'in_speed': history.in_speed, 'out_speed': history.out_speed} for
                      history in record]})


def check_utc_timestamp():
    try:
        start = int(request.args.get('start', ''))
        end = int(request.args.get('end', ''))
    except Exception as e:
        return 0, 0, False, str(e)
    if start > end:
        return 0, 0, False, 'start time larger than end time'
    return start, end, True, ''

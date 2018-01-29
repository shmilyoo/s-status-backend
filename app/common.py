from datetime import datetime, timezone


def get_timestamp_utcnow():
    return int(datetime.utcnow().replace(tzinfo=timezone.utc).timestamp())

from typing import Union

from datetime import datetime, timezone

timezone.utc

TIMESTAMP_FORMATS = [
    '%Y-%m-%dT%H:%M:%S.%fZ',
    '%Y-%m-%dT%H:%M:%S.%f',
    '%Y-%m-%dT%H:%M:%S',
]


def parse_timestamp(timestamp: Union[int, str], raw=False):
    """
    Receives a timestamp value (which can be a string or a numeric value)
    and parses it into the correct UTC timestamp representation.
    """
    parsed_timestamp = None
    if isinstance(timestamp, int):
        try:
            parsed_timestamp = datetime.fromtimestamp(timestamp, timezone.utc)
        except ValueError:
            parsed_timestamp = datetime.fromtimestamp(timestamp/1000, timezone.utc)
    elif isinstance(timestamp, str):
        timestamp = timestamp.replace("'", "")
        for format in TIMESTAMP_FORMATS:
            try:
                parsed_timestamp = datetime.strptime(timestamp, format)
                break
            except ValueError:
                continue
        if not parsed_timestamp:
            raise ValueError("Cannot parse", timestamp)
    else:
        raise ValueError("Input format is unknown.")

    return parsed_timestamp if raw else parsed_timestamp.isoformat(timespec='milliseconds')

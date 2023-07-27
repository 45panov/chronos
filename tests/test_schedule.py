from typing import Optional

from chronos import *


def test_schedule_false():
    SCHEDULE = False
    DEFAULT_TIME: int = 777 if not SCHEDULE else {
        'Monday': 0,
        'Tuesday': 0,
        'Wednesday': 0,
        'Thursday': 0,
        'Friday': 0,
        'Saturday': 0,
        'Sunday': 0,
    }.get(datetime.today().strftime('%A'))
    assert DEFAULT_TIME == 777, "DEFAULT_TIME must be equal to 0"

def test_schedule_true():
    SCHEDULE = True
    DEFAULT_TIME: int = 777 if not SCHEDULE else {
        'Monday': 0,
        'Tuesday': 0,
        'Wednesday': 0,
        'Thursday': 0,
        'Friday': 0,
        'Saturday': 0,
        'Sunday': 0,
    }.get(datetime.today().strftime('%A'))
    assert DEFAULT_TIME == 0, "DEFAULT_TIME must be equal to 0"

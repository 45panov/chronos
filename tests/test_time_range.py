from chronos import *
import pytest

""" Here test time range in which target USER is allowed to login.  """


def test_time_range_dict():
    assert type(TIME_RANGE) == tuple, "TIME_RANGE must be dict."

def test_time_range_elements_are_strings():
    for _ in TIME_RANGE:
        assert type(_) == str, "TIME_RANGE elements must be str."

# Test various now_time values to match TIME_RANGE
@pytest.mark.parametrize(
    'now_time_samples, expected_result',
    [(time(8,0), False),
     (time(10,0), True),
     (time(18,0), True),
     (time(23,00), False)]
    
)
def test_is_now_in_time_range(now_time_samples, expected_result):
    a = is_now_in_time_range(*TIME_RANGE, now_time_samples) 
    assert a == expected_result, f"Result is {a}. Expected {expected_result}"

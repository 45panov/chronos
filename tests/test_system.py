from chronos import *

def test_system_return_timer():
    timer = System().set_timer(1)
    assert timer.remain == Timer(1).remain

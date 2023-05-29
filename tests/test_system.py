from chronos import *
import pytest


def test_system_return_timer():
    jdata = DataStorage()
    timer = System().set_timer(jdata.time_remain)
    assert timer.remain == Timer(10).remain, "System().set_timer() must return Timer object"


def test_system_performs_logout():
    assert System.logout() == "os.system(" + System()._LOGOUT_COMMANDS[os.name] + ")"

from chronos import *

def test_timer_1():
    timer = Timer(1)
    assert timer.remain == 1


def test_chronos_reduces_timer():
    timer = Timer(2)
    Chronos.run(timer)
    assert timer.is_run == False, "timer.is_run must be False after Chronos has reduced it to 0"


def test_timer_is_0():
    timer = Timer(0)
    Chronos.run(timer)
    assert timer.is_run == False, 'timer.is_run must be False if Timer(0)'


def test_logout_on_timer_is_0():
    jdata = JData()
    timer = System().set_timer(jdata.time_remain)
    Chronos.run(timer)
    assert System.logout() == "os.system(" + System().LOGOUT_COMMANDS[os.name] + ")"

def test_timer_is_run():
    timer = Timer(10)
    assert timer

def test_timer_0_is_false():
    timer = Timer(0)
    assert not timer





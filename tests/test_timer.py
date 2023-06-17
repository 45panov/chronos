from chronos import *


def test_timer_1():
    storage = Storage()
    storage.time_remain = 1
    timer = Timer(storage)
    assert timer.remain == 1


def test_chronos_reduces_timer():
    timer = Timer(Storage())
    Chronos.run(timer)
    assert timer.remain == 0, "timer.is_run must be False after Chronos has reduced it to 0"


def test_timer_is_0():
    timer = Timer(Storage())
    Chronos.run(timer)
    assert timer.remain == 0, 'timer.is_run must be False if Timer(0)'


def test_logout_on_timer_is_0():
    jdata = Storage()
    timer = Timer(jdata)
    Chronos.run(timer)
    assert Core.logout() == "os.system(" + Core()._LOGOUT_COMMANDS[os.name] + ")"


def test_timer_is_run():
    timer = Timer(Storage())
    assert timer


def test_timer_0_is_false():
    storage = Storage()
    storage.time_remain = 0
    timer = Timer(storage)
    assert bool(timer) == False


def test_timer_set_from_storage():
    storage = Storage()
    timer = Timer(storage)
    assert timer.remain == 10, "Timer.remain must be equal to 10"

def test_timer_check_date():
    storage = Storage()
    temp = storage.last_date[:-1]
    storage.last_date = temp + '0'
    timer = Timer(storage)
    assert storage.last_date == Core.current_date

def test_storage_reset():
    storage = Storage()
    storage.last_date = '00000000'
    storage.reset()
    assert storage.last_date == Core.current_date, "Storage.reset() must equalaze last_date to current_date"


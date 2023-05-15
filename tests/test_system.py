from chronos import *

def test_system_return_timer():
    j_data = JData().read()
    timer = System().set_timer(j_data.time_remain)
    assert timer.remain == Timer(10).remain, "System().set_timer() must return Timer object"

def test_system_performs_logout():
    assert System.logout() == "os.system(" + System().LOGOUT_COMMANDS[os.name] + ")"




from chronos import *

def test_system_return_timer():
    j_data = JData()
    j_data = {'remaining_time': 1}
    timer = System().set_timer(j_data['remaining_time'])
    assert timer.remain == Timer(1).remain, "System().set_timer() must return Timer object"

def test_system_performs_logout():
    assert System.logout() == "os.system(" + System().LOGOUT_COMMANDS[os.name] + ")"




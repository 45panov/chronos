from chronos import *

def test_system_return_timer():
    timer = System().set_timer(1)
    assert timer.remain == Timer(1).remain, "System().set_timer() must return Timer object"

def test_system_performs_logout():
    assert System().logout() == "os.system(System().logout_command())"


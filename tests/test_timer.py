from chronos import *

def test_not_logout_on_timer_remain_1():
    timer = Timer(1)
    assert not Chronos.logout(timer) == "os.system(System().logout_command())", "Chronos.logout(timer) must be NOT equal" \
                                                                                "to os.system(System().logout_command())"

# def test_chronos_return_timer_object():
#     timer = Timer(2)
#     assert Chronos.logout(timer) == Timer(1), "Chronos.logout(timer(2)) must return Timer object"
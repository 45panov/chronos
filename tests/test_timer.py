from chronos import *

def test_not_logout_on_timer_remain_1():
    timer = Timer(1)
    assert not Chronos.logout(timer) == "os.system(System().logout_command())", "Chronos.logout(timer) must be NOT equal" \
                                                                                "to os.system(System().logout_command())"

def test_timer_zero():
    timer = Timer(0)
    assert Chronos.logout(timer) == "os.system(System().logout_command())", "Chronos must logout on Timer(0)"

def test_timer_run():
    timer = Timer(1)
    timer.run()
    assert Chronos.logout(timer) == "os.system(System().logout_command())", "Chronos must logout on Timer(0)"
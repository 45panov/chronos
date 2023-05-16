from chronos import *

def test_system_return_timer():
    jdata = JData()
    timer = System().set_timer(jdata.time_remain)
    assert timer.remain == Timer(10).remain, "System().set_timer() must return Timer object"

def test_system_performs_logout():
    assert System.logout() == "os.system(" + System().LOGOUT_COMMANDS[os.name] + ")"

<<<<<<< HEAD


=======
>>>>>>> be58584e206988a1dae835d9f27400fe1f1ec1d9



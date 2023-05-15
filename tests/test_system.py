from chronos import *

def test_system_return_timer():
    timer = System().set_timer(1)
    assert timer.remain == Timer(1).remain, "System().set_timer() must return Timer object"

def test_system_performs_logout():
    assert System.logout() == "os.system(" + System().LOGOUT_COMMANDS[os.name] + ")"

def test_system_get_time():
    file_data = {'current_date': '20230511',
                 'remaining_time': 10}

    timer = System().set_timer(file_data['remaining_time'])
    Chronos.run(timer)
    System.logout()
    assert System.logout() == "os.system(" + System().LOGOUT_COMMANDS[os.name] + ")"




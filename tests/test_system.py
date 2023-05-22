from chronos import *
import pytest

def test_system_return_timer():
    jdata = JData()
    timer = System().set_timer(jdata.time_remain)
    assert timer.remain == Timer(10).remain, "System().set_timer() must return Timer object"

def test_system_performs_logout():
    assert System.logout() == "os.system(" + System().LOGOUT_COMMANDS[os.name] + ")"

@pytest.mark.parametrize('test_os, expected', [('posix', "/etc/cjdata.json"), 
                                               ('nt', "$TMP/cjdata.json")])
def test_path_to_cjdata(test_os, expected):
    if os.name == test_os:
        assert System.path_to_cjdata() == expected 

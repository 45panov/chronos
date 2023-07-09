from chronos import *
import pytest

def test_system_performs_logout():
    if not PRODUCTION:
        assert Core.logout() == f"os.system(\"{LOGOUT_COMMANDS[os.name]}\")"

def test_switch_test_to_prod():
    """ Test switching between test and production modes. """
    if not PRODUCTION:
        assert Core.logout() == f"os.system(\"{LOGOUT_COMMANDS[os.name]}\")"



# def test_system_keeps_pair_logout_and_path_to_storage():
#     if os.name == 'nt':
#         assert System.path_to_storage(), System.logout() == os.environ['TMP'] + r'\storage.json', 'shutdown -l'

# def test_system_return_timer():
#     jdata = Storage()
#     timer = Core().set_timer(jdata.time_remain)
#     assert timer.remain == Timer(10).remain, "System().set_timer() must return Timer object"

from chronos import *

# def test_logout():
#     assert Chronos.logout() == "os.system(System().logout_command())"

def test_imports():
    assert 'os' in globals(), "os must be in globals"
    assert 'time' in globals(), "time must be in globals"

def test_logout_commands():
    assert System.logout_command() == "shutdown -l"

def test_linux_logout_cmd():
    assert System().LOGOUT_COMMANDS['posix'] == f"pkill -kill -u {os.getlogin()}"






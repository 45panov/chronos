from chronos import *

# def test_logout():
#     assert Chronos.logout() == "os.system(System().logout_command())"

def test_imports():
    assert 'os' in globals(), "os must be in globals"
    assert 'time' in globals(), "time must be in globals"
    assert 'json' in globals(), "json must be in globals"






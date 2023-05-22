from chronos import *
import pytest

@pytest.mark.parametrize('test_os, expected', [('posix', "/tmp/cjdata.json"),
                                               ('nt', os.getenv('TMP') +  r'\cjdata.json')])
def test_no_data_file(test_os, expected):
   jdata = JData()
   # assert jdata.time_remain == 10
   if os.name == test_os:
       assert os.path.exists(expected) == True


def test_cjdata_is_empty():
    os.system("rm tmp/cjdata.json && touch tmp/cjdata.json")
    jdata = JData()
    assert jdata.time_remain == 10, "cjdata.json can not be empty"



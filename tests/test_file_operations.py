from chronos import *
import pytest


@pytest.mark.parametrize('test_os, expected', [('posix', "/tmp/cjdata.json"),
                                               ('nt', os.getenv('TMP') + r'\cjdata.json')])
def test_no_data_file(test_os, expected):
    jdata = JData()
    # assert jdata.time_remain == 10
    if os.name == test_os:
        assert os.path.exists(expected) == True


@pytest.mark.parametrize('test_os, create_empty_cjdata',
                         [('posix', "rm tmp/cjdata.json && touch tmp/cjdata.json"),
                          ('nt', "del " + System.path_to_cjdata() + "; copy /b NUL " + System.path_to_cjdata())])
def test_cjdata_is_empty(test_os, create_empty_cjdata):
    if os.name == test_os:
        os.system(create_empty_cjdata)
        jdata = JData()
        assert jdata.time_remain == 10, "cjdata.json can not be empty"

from chronos import *

def test_no_data_file():
   jdata = JData()
   assert jdata.time_remain == 10 
   assert os.path.exists("/tmp/cjdata.json") == True


def test_cjdata_is_empty():
    os.system("rm tmp/cjdata.json && touch tmp/cjdata.json")
    jdata = JData()
    assert jdata.time_remain == 10, "cjdata.json can not be empty"



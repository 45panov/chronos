from chronos import *
import pytest

def test_storage_is_DataStorage():
    storage = DataStorage()
    assert isinstance(storage, DataStorage)

def test_storage():
    storage = DataStorage()
    assert storage.time_remain == 10

def test_no_storage_file():
    if os.name == 'posix':
        os.system("rm -f " + System.path_to_storage())
        storage = DataStorage()
        assert storage.time_remain == 10

    if os.name == 'nt':
        os.system("del " + System.path_to_storage())
        storage = DataStorage()
        assert storage.time_remain == 10
        

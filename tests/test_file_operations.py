from chronos import *
import pytest


def test_storage_is_DataStorage():
    storage = Storage()
    assert isinstance(storage, Storage)


def test_storage():
    storage = Storage()
    assert isinstance(storage.time_remain, int), "Storage.time_remain must be an instance of int"


def test_no_storage_file():
    if os.name == 'posix':
        os.system("rm -f " + STORAGE)
        storage = Storage()
        assert storage.time_remain == DEFAULT_TIME

    if os.name == 'nt':
        os.system("del " + STORAGE)
        storage = Storage()
        assert storage.time_remain == DEFAULT_TIME


@pytest.mark.parametrize(
    'os_name, expected_storage_path', [
        ('posix', '/var/tmp/storage_'+USER+'.json'),
        ('nt', f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\storage.json")
    ]
)
def test_storage_path(os_name, expected_storage_path):
    """"
        Tests following directories accessability:
            for Linux: tmp/storage.json
            for Windows: $TMP/storage.json
    """

    if os.name == os_name:
        assert STORAGE == expected_storage_path

def test_get_date_from_storage():
    storage = Storage()
    assert storage.last_date == CURRENT_DATE


def test_save_state():
    storage = Storage()
    timer = Timer(storage)
    storage.save(3, CURRENT_DATE)
    storage = Storage()
    assert storage.time_remain == 3, "storage.time_remain must be equal to 10 after storage.save(10)"





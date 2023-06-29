from chronos import *
import pytest


def test_storage_is_DataStorage():
    storage = Storage()
    assert isinstance(storage, Storage)


def test_storage():
    storage = Storage()
    assert storage.time_remain == 10


def test_no_storage_file():
    if os.name == 'posix':
        os.system("rm -f " + Core.path_to_storage())
        storage = Storage()
        assert storage.time_remain == 10

    if os.name == 'nt':
        os.system("del " + Core.path_to_storage())
        storage = Storage()
        assert storage.time_remain == 10


@pytest.mark.parametrize(
    'os_name, expected_storage_path', [
        ('posix', '/tmp/storage.json'),
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
        storage = Storage()
        assert storage.path_to_storage() == expected_storage_path

def test_get_date_from_storage():
    storage = Storage()
    assert storage.last_date == time.strftime("%d%m%Y", time.gmtime())


def test_save_state():
    storage = Storage()
    timer = Timer(storage)
    storage.save(3, Core.current_date)
    storage = Storage()
    assert storage.time_remain == 3, "storage.time_remain must be equal to 10 after storage.save(10)"





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
        ('nt', os.environ['TMP'] + r'\storage.json')
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


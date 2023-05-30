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
        storage = DataStorage()
        assert storage.path_to_storage() == expected_storage_path

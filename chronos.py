import time
import os
import pickle
from sys import exit
from typing import Protocol

PRODUCTION = False  # If set to 1 Chronos will perform former logout command.

USER = "afanasiy"  # Account for which Chronos should perform logout command.

DEFAULT_TIME = 5800  # Time in seconds pass before Chronos perform logout.

STORAGE_FILE_PATH = os.path.expanduser("~") + "/chronos/storage.pkl"

LOGOUT_COMMANDS = {"posix": "pkill -kill -u " + USER, "nt": "shutdown -l"}


class SecondsStorageProtocol(Protocol):
    def load(self) -> int:
        ...

    def save(self, seconds: int) -> None:
        ...


class SecondsStorage(SecondsStorageProtocol):
    def __init__(self, file_path: str, default_value=DEFAULT_TIME):
        self._file_path = file_path
        self._default_value = default_value

    def save(self, seconds: int) -> None:
        with open(self._file_path, "wb") as file:
            pickle.dump(seconds, file)

    def load(self) -> int:
        if not os.path.exists(self._file_path) or os.stat(self._file_path).st_size == 0:
            return self._default_value

        with open(self._file_path, "rb") as file:
            result = pickle.load(file)
        return result


class Timer:
    SECONDS_PER_ITERATION = 1

    def __init__(self, storage: SecondsStorageProtocol):
        self._storage = storage

    def run(self):
        seconds_left = self._storage.load()
        while seconds_left > 0:
            time.sleep(self.SECONDS_PER_ITERATION)
            seconds_left -= self.SECONDS_PER_ITERATION
            self._storage.save(seconds_left)


if __name__ == "__main__":
    timer = Timer(storage=SecondsStorage(file_path=STORAGE_FILE_PATH))
    timer.run()
    if not PRODUCTION:
        print("Chronos finished its job in test mode")
        exit()
    os.system(f"{LOGOUT_COMMANDS[os.name]}")

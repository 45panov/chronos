import json
import time
import os
from json import JSONDecodeError


class System:
    # Keeps logout commands for different OS
    _LOGOUT_COMMANDS = {'posix': f"pkill -kill -u {os.getlogin()}",
                        'nt': "shutdown -l"}

    if os.name == 'posix':
        _STORAGE_FILE = '/tmp/storage.json'
    if os.name == 'nt':
        _STORAGE_FILE = os.environ['TMP'] + r'\storage.json'

    @classmethod
    def path_to_storage(cls):
        return cls._STORAGE_FILE

    @classmethod
    def logout(cls):
        return "os.system(" + cls._LOGOUT_COMMANDS[os.name] + ")"  # Strip quotes on production

    def set_timer(self, seconds):
        return Timer(seconds)


class Timer:
    def __init__(self, seconds: int):
        self.remain = seconds

    def __bool__(self):
        return False if self.remain == 0 else True


class DataStorage(System):
    def __init__(self):
        if os.path.exists(self.path_to_storage()):
            with open(self.path_to_storage(), mode='r+') as f:
                try:
                    self.time_remain = json.load(f)
                except JSONDecodeError:
                    self.time_remain = 10
                    json.dump(self.time_remain, f)


        else:
            with open(self.path_to_storage(), mode='w') as f:
                self.time_remain = 10
                json.dump(self.time_remain, f)


class Chronos:
    def run(timer: Timer):
        while timer:
            timer.remain -= 1
        return timer

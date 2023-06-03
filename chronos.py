import json
import time
import os
from tempfile import gettempdir
from json import JSONDecodeError


class Core:
    # Keeps logout commands for different OS
    _LOGOUT_COMMANDS = {'posix': f"pkill -kill -u {os.getlogin()}",
                        'nt': "shutdown -l"}

    _STORAGE = gettempdir() + os.sep + 'storage.json'

    @classmethod
    def path_to_storage(cls):
        if not os.path.exists(cls._STORAGE):
            with open(cls._STORAGE, mode='w') as f:
                pass
        return cls._STORAGE

    @classmethod
    def logout(cls):
        return "os.system(" + cls._LOGOUT_COMMANDS[os.name] + ")"  # Strip quotes on production

    def set_timer(self, seconds):
        return Timer(seconds)


class Storage(Core):
    def __init__(self):
        with open(self.path_to_storage(), mode='r+') as f:
            try:
                json_data = json.load(f)
                self.time_remain = json_data.get('time_remain')
            except (JSONDecodeError, ValueError):
                # Here must be log entry
                self.time_remain = 10
                json_data = {
                    'time_remain': self.time_remain
                }
                json.dump(json_data, f)


class Timer:
    def __init__(self, seconds: int):
        self.remain = seconds

    def __bool__(self):
        return False if self.remain == 0 else True


class Chronos:
    def run(timer: Timer):
        while timer:
            timer.remain -= 1
        return timer

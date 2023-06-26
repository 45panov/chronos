import json
import time
import os
from tempfile import gettempdir
from json import JSONDecodeError

""" While PRODUCTION is False Cronos runs in test mode. It returns
logout command as a string variable. When PRODUCTION is True Cronos 
performs former logout command."""
PRODUCTION = False

class Core: # Here must be log entry
    # Keeps logout commands for different OS
    _LOGOUT_COMMANDS = {'posix': f"pkill -kill -u {os.getlogin()}",
                        'nt': "shutdown -l"}
    # Keeps path to storage file
    _STORAGE = gettempdir() + os.sep + 'storage.json'

    default_time = 10

    current_date = time.strftime("%d%m%Y", time.gmtime())

    @classmethod
    def path_to_storage(cls):
        """ Returns path to storage.json file or creates it if it doesn't exist. """
        if not os.path.exists(cls._STORAGE):
            try:
                with open(cls._STORAGE, mode='w') as f:
                    pass
            except PermissionError:
                pass  # Here must be log entry
        return cls._STORAGE

    @classmethod
    def logout(cls):
        """ Performs platform depending logout command. """
        if PRODUCTION:
            os.system(f"{cls._LOGOUT_COMMANDS[os.name]}")
        else:
            return "os.system(" + cls._LOGOUT_COMMANDS[os.name] + ")"  


class Storage(Core):
    def __init__(self):
        with open(self.path_to_storage(), mode='r+') as f:
            try:
                self.time_remain, self.last_date = json.load(f).values()
            except (JSONDecodeError, ValueError):
                # Here must be log entry
                self.reset()

    def reset(self):
        """ Loads default Core.current_date and Core.default_time to storage.json """
        with open(self.path_to_storage(), mode='w') as f:
            self.last_date, self.time_remain = super().current_date, super().default_time
            json.dump({'time_remain': super().default_time,
                       'last_date': super().current_date}, f)


class Timer:
    def __init__(self, storage: Storage):
        if storage.last_date != Core.current_date:
            storage.reset()
        self.remain = storage.time_remain

    def __bool__(self):
        return False if self.remain == 0 else True

    def run(self):
        while self.remain > 0: self.remain -= 1
        return None

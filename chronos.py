import json
import time
import os
from tempfile import gettempdir
from json import JSONDecodeError

""" While PRODUCTION is 0 Chronos runs in test mode. It returns
logout command as a string variable. When PRODUCTION is 0 Chronos 
performs former logout command."""
PRODUCTION = 0

""" DEFAULT_TIME is the time in seconds which pass before Chronos performs logout. """
DEFAULT_TIME = 10

class Core: # Here must be log entry
    # Keeps logout commands for different OS
    _LOGOUT_COMMANDS = {'posix': f"pkill -kill -u {os.getlogin()}",
                        'nt': "shutdown -l"}
    # Keeps path to storage file
    _STORAGE = gettempdir() + os.sep + 'storage.json'

    # default_time = DEFAULT_TIME

    current_date = time.strftime("%d%m%Y", time.gmtime())

    @classmethod
    def path_to_storage(cls):
        """ Creates storage.json file or returns its path if one already exists. """
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
            self.last_date, self.time_remain = super().current_date, DEFAULT_TIME
            json.dump({'time_remain': DEFAULT_TIME,
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


# Main part starts here.
Timer(Storage()).run()
Core.logout()

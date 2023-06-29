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


class Core:  # Here must be log entry
    # Keeps logout commands for different OS
    _LOGOUT_COMMANDS = {'posix': f"pkill -kill -u {os.getlogin()}",
                        'nt': "shutdown -l"}
    # Keeps path to storage file
    _STORAGE = gettempdir() + os.sep + 'storage.json'

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

    def save(self, time_value: int, date_value: str) -> None:
        with open(self.path_to_storage(), mode='w') as f:
            json.dump({'time_remain': time_value, 'last_date': date_value}, f)

    def reset(self) -> None:
        """ Loads default Core.current_date and Core.default_time to storage.json """
        self.time_remain, self.last_date  = DEFAULT_TIME, super().current_date,
        self.save(self.time_remain, self.last_date)


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

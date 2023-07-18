import json
import time
import os
from sys import exit
from tempfile import gettempdir


PRODUCTION = 0  # If set to 1 Chronos will perform former logout command.

USER = 'afanasiy'  # Account for which Chronos should perform logout command.

DEFAULT_TIME = 5800  # Time in seconds pass before Chronos perform logout.

STORAGE = {'posix': '/var/tmp/storage.json',
           'nt': gettempdir()+'\\storage.json'
           }.get(os.name)

CURRENT_DATE = time.strftime("%d%m%Y", time.localtime())

LOGOUT_COMMANDS = {"posix": "pkill -kill -u " + USER, "nt": "shutdown -l"}


class Storage():
    def __init__(self):
        if not os.path.exists(STORAGE) or os.stat(STORAGE).st_size == 0:
            self.time_remain, self.last_date = DEFAULT_TIME, CURRENT_DATE
            self.save(self.time_remain, self.last_date)
        else:
            with open(STORAGE, mode='r', encoding='utf-8') as f:
                self.time_remain, self.last_date = json.load(f).values()

    def save(self, time_value: int, date_value: str) -> None:
        """Takes time and date values and loads it to storage.json"""
        with open(STORAGE, mode='w', encoding='utf-8') as f:
            json.dump({"time_remain": time_value, "last_date": date_value}, f)
            f.flush()


class Timer:
    def __init__(self, storage: Storage):
        if storage.last_date != CURRENT_DATE:
            storage.time_remain, storage.last_date = DEFAULT_TIME, CURRENT_DATE
            storage.save(DEFAULT_TIME, CURRENT_DATE)
        self.remain = storage.time_remain
        self.save = storage.save

    def __bool__(self):
        return True if self.remain != 0 else False

    def run(self):
        if self.remain > 0:
            self.remain -= 1
            if self.remain % 10 == 0:  # Save timer state every 10 seconds
                self.save(self.remain, CURRENT_DATE)
            time.sleep(1 if PRODUCTION else 0)
            return self.remain
        return self.remain


# Main part starts here.
if __name__ == '__main__':
    storage = Storage()
    timer = Timer(storage)
    while timer:
        timer.run()
    if not PRODUCTION and not timer:
        print('Chronos finished its job in test mode')
        exit()
    os.system(f"{LOGOUT_COMMANDS[os.name]}")

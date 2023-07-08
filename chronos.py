import logging
import json
import time
import os
from tempfile import gettempdir
from json import JSONDecodeError

try:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=os.path.abspath(os.path.dirname(__file__)) + os.sep + "log.log",
    )
except:
    raise Exception("Logging error!")
logging.debug("---FILE CHRONOS.PY OPENED, LOGGING STARTED---")

""" While PRODUCTION is 0 Chronos runs in test mode. It returns
logout command as a string variable. When PRODUCTION is 0 Chronos 
performs former logout command."""
PRODUCTION = 0

""" DEFAULT_TIME is the time in seconds which pass before Chronos performs logout. """
DEFAULT_TIME = 10

STORAGE = os.path.abspath(os.path.dirname(__file__)) + os.sep + "storage.json"


class Core:  # Here must be log entry
    # Keeps logout commands for different OS
    _LOGOUT_COMMANDS = {"posix": f"pkill -kill -u {os.getlogin()}", "nt": "shutdown -l"}

    # Keeps path to storage file

    current_date = time.strftime("%d%m%Y", time.localtime())

    @classmethod
    def path_to_storage(cls):
        """Creates storage.json file or returns its path if one already exists."""
        if not os.path.exists(STORAGE):
            try:
                with open(STORAGE, mode="w") as f:
                    json.dump({"time_remain": DEFAULT_TIME, "last_date": cls.current_date}, f)
            except PermissionError:
                logging.debug("Permission error in Core.path_to_storage().")
        return STORAGE

    @classmethod
    def logout(cls):
        """Performs platform depending logout command."""
        if PRODUCTION:
            os.system(f"{cls._LOGOUT_COMMANDS[os.name]}")
        return f"os.system(\"{cls._LOGOUT_COMMANDS[os.name]}\")"


class Storage(Core):
    def __init__(self):
        with open(self.path_to_storage(), mode="r+") as f:
            try:
                self.time_remain, self.last_date = json.load(f).values()
                logging.debug(f"Storage loaded {self.time_remain} and {self.last_date}.")
            except (JSONDecodeError, ValueError):
                logging.debug("JSONDecodeError or Value error in Storage.__init__()")
                self.reset()

    def save(self, time_value: int, date_value: str) -> None:
        """Takes time and date values and loads it to storage.json"""
        with open(self.path_to_storage(), mode="w") as f:
            try:
                json.dump({"time_remain": time_value, "last_date": date_value}, f)
            except:
                logging.debug("json.dump failed in Storage.save")

    def reset(self) -> None:
        """Loads default Core.current_date and Core.default_time to storage.json"""
        self.time_remain, self.last_date = (
            DEFAULT_TIME,
            super().current_date,
        )

        self.save(self.time_remain, self.last_date)


class Timer:
    def __init__(self, storage: Storage):
        if storage.last_date != Core.current_date:
            storage.reset()
            # storage.__init__()
        self.remain = storage.time_remain
        self.save = storage.save

    def __bool__(self):
        return True if self.remain != 0 else False

    def run(self):
        logging.debug("Timer.run()")
        if self.remain > 0:
            self.remain -= 1
            logging.debug(f"Tiimer is running with remain={self.remain}")
            if self.remain % 10 == 0:  # Save timer state every 10 seconds
                self.save(self.remain, Core.current_date)
            time.sleep(1 if PRODUCTION else 0)
            return self.remain
        logging.debug("Timer is 0")
        return self.remain


# Main part starts here.
if __name__ == "__main__":
    logging.debug("Chronos main part started.")
    storage = Storage()
    timer = Timer(storage)
    while timer:
        timer.run()
    if PRODUCTION and not timer:
        logging.debug("Chronos performs former logout and finishes its job.")
        Core.logout()
    elif not PRODUCTION and not timer:
        print("Chronos finished its job in test  mode.")
SystemExit()

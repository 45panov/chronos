import os
import time
import json


default_user = "tihonasiy"
default_time = 7200
date_time_file = os.path.expanduser("~") + "/chronos/date_time.json"


def timer():

    # Reads remaining time from date_time.json and decreases
    # its value in each iterration.

    with open(date_time_file, mode="r", encoding="utf-8") as f:

        json_entry = json.load(f)

    while json_entry["remaining_time"] > 0:

        with open(date_time_file, mode="w", encoding="utf-8") as f:

            json_entry["remaining_time"] -= 1

            json.dump(json_entry, f)

            f.flush()

            time.sleep(1)


def reset_date_and_timer():

    # Updates current date in date_time.json

    with open(date_time_file, mode="w", encoding="utf-8") as f:

        json_entry = {
            "current_date": time.strftime("%Y%m%d", time.gmtime()),
            "remaining_time": default_time,
        }

        json.dump(json_entry, f)

        f.flush()


# Main part starts below.


if os.path.exists(date_time_file) == False or os.stat(date_time_file).st_size == 0:

    # Creates file with date and time if it doesn't exist or empty.

    reset_date_and_timer()

    with open(date_time_file, mode="r", encoding="utf-8") as f:

        json_entry = json.load(f)


else:  # Reads data from date_time_file.

    with open(date_time_file, mode="r", encoding="utf-8") as f:

        json_entry = json.load(f)


if json_entry["current_date"] == time.strftime("%Y%m%d", time.gmtime()):

    # Compare last saved and current dates.

    timer()

    os.system("pkill -KILL -u {0}".format(default_user))


else:

    reset_date_and_timer()

    timer()

    os.system("pkill -KILL -u {0}".format(default_user))

import os, time, json


class System:
    LOGOUT_COMMANDS = {'posix': f"pkill -kill -u {os.getlogin()}",  # Keeps logout commands for different OS
                       'nt': "shutdown -l"}
    
    PATH_TO_CJDATA = {'posix': "/etc/cjdata.json", # Keeps paths to cjdata.json for different OS
                      'nt': "$TMP/cjdata.json"}

    @classmethod
    def logout(cls):
        return "os.system(" + cls.LOGOUT_COMMANDS[os.name] + ")"
       
    @classmethod
    def path_to_cjdata(cls):
        return cls.PATH_TO_CJDATA[os.name]

    def set_timer(self, seconds):
        return Timer(seconds)


class Timer:
    def __init__(self, seconds: int):
        self.is_run = False
        self.remain = seconds

class JData():
    def __init__(self):
        if os.path.exists('/tmp/cjdata.json') and os.stat('/tmp/cjdata.json') != 0:
            with open("/tmp/cjdata.json") as f:
                self.time_remain = json.load(f)
        else:        
            with open("/tmp/cjdata.json", mode='w') as f:
                self.time_remain = 10
                json.dump(self.time_remain, f)


class Chronos:
    def run(timer: Timer):
        timer.is_run = True
        while timer.remain > 0:
            timer.remain -= 1
        timer.is_run = False
        return timer




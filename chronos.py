import os, time


class System:
    LOGOUT_COMMANDS = {'posix': f"pkill -kill -u {os.getlogin()}",  # Keeps logout commands for different OS
                       'nt': "shutdown -l"}

    def set_timer(self, seconds):
        return Timer(seconds)

    @classmethod
    def logout(cls):
        return "os.system(" + cls.LOGOUT_COMMANDS[os.name] + ")"
       

class Timer:
    def __init__(self, seconds: int):
        self.is_run = False
        self.remain = seconds

class JData():
    def read(self):
        self.time_remain = 10

class Chronos:
    def run(timer: Timer):
        timer.is_run = True
        while timer.remain > 0:
            timer.remain -= 1
        timer.is_run = False
        return timer




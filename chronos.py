import os, time


class System:
    LOGOUT_COMMANDS = {'posix': f"pkill -kill -u {os.getlogin()}",  # Keeps logout commands for different OS
                       'nt': "shutdown -l"}

    @classmethod
    def logout_command(cls):  # Gets logout command for particular OS
        return cls.LOGOUT_COMMANDS[os.name]

    def set_timer(self, seconds):
        return Timer(seconds)

class Timer:
    def __init__(self, seconds: int):
        self.remain = seconds

    def run(self):
        self.remain -= 1


class Chronos:
    def logout(timer: Timer):  # Runs logout command
        if not timer.remain:
            return "os.system(System().logout_command())"  # Change to os.system(System().logout_command()


timer = Timer(1)
timer.run()
print(Chronos.logout(timer))

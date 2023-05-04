import os


class System:
    LOGOUT_COMMANDS = {'posix': f"pkill -kill -u {os.getlogin()}", # Keeps logout commands for different OS
                       'nt': "shutdown -l"}

    @classmethod
    def logout_command(cls): # Gets logout command for particular OS
        return cls.LOGOUT_COMMANDS[os.name]


class Timer:
    def __init__(self, seconds: int):
        self.remain = seconds

class Chronos:
    def logout(timer: Timer): # Runs logout command
        if not timer.remain:
            return "os.system(System().logout_command())" # Change to os.system(System().logout_command()

print(Chronos.logout(Timer(3)))
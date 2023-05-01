import os


class System:
    LOGOUT_COMMANDS = {'posix': f"pkill -kill -u {os.getlogin()}",
                       'nt': "shutdown -l"}

    @classmethod
    def logout_command(cls):
        return cls.LOGOUT_COMMANDS[os.name]


class Chronos:
    def logout():
        return "os.system(System().logout_command())" # Change to os.system(System().logout_command())

print(Chronos.logout())
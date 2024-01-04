# CHRONOS 0.4

Chronos is pyton-script to limit my children playinig PC games.

It performes logout from USER when time defined in DEFAULT_TIME expires. You can set it up in chronos.py directly.
When date is changed Chronos automatically resets remaining time according to DEFAULT_TIME.

To keep current date and remaining time Chronos creates storage.json in '/var/tmp/' in Linux and something like 
'C:\Users\%USER%\Appdata\Local\Temp\' in Windows. To add or reduce remaining time you can edit corresponding variable 
in storage.json. 

Tested on Linix Mint 19.3 and Windows 10 with Python 3.6.8. 


## New in version 0.4

Now you can set up a period in TIME_RANGE variable in which USER is allowed to login.


## INSTALLATION

Clone repo or copy chronos.py to directoty from which it may be executed under target account.
Make chronos.py run on system start under target USER account. For example in Linux you may add following
line in target USER's .profile:

_python ~/chronos/chronos.py_

Set up USER, DEFAULT_TIME (SCHEDULE if neccessery) and switch PRODUCTION to True in chronos.py. Reboot and login USER
account.


### CHANGELOG

New in version 0.3.
SCHEDULE option is implemented. If SCHEDULE is True, DEFAULT_TIME is being set in accordance with 
time set for particular day of week. Othewise DEFAULT_TIME is same for any day.

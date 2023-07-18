# CHRONOS 0.2

Chronos is pyton-script to limit my children playinig PC games.

It performes logout from USER when time defined in DEFAULT_TIME expires. You can set it up in chronos.py directly.
When date is changed Chronos automatically resets remaining time according to DEFAULT_TIME.

To keep current date and remaining time Chronos creates storage.json in '/var/tmp/' in Linux and something like 
'C:\Users\%USER%\Appdata\Local\Temp\' in Windows. To add or reduce remaining time you can edit corresponding variable 
in storage.json. 

Tested on Linix Mint 19.3 and Windows 10 with Python 3.6.8. 

### INSTALLATION

Clone repo of copy chronos.py to directoty from which it may be executed under target account.
Make chronos.py run on system start under target account. For example in Linux you may add following
line in target user's .profile:

_python ~/chronos/chronos.py_

Set up USER, DEFAULT_TIME and switch PRODUCTION to True in chronos.py. Reboot and login USER account.




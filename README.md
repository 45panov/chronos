#chronos 0.1

chronos.py is script to limit my children playinig PC games.

chronos.py performes logout from default_user  when time, defined in default_time, has expired.

It creates date_time.json to store current date and remaining time.

It's created under Linix Mint 19.3 and python ver 3.6

To provide chronos execution on system login  the following command should be added to /home/.profile of corresponding user:

python3 /home/USERNAME/chronos.py &



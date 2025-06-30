@echo off
echo Starting Lucien Proxy...

:: Εκκίνηση Lucien Bot
start /min python lucien_bot.py

:: Εκκίνηση Telegram Command Listener
start /min python telegram_command_listener.py

:: Εκκίνηση Watchdog Token Checker
start /min python lucien_watchdog.py

exit

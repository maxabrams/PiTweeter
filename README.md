# PiTweeter
Python script to tweet status information about the Raspberry Pi!

This simple python program demonstrates twitter api on the Raspberry Pi. When ran, this will tweet cpu temp, free disk space, cpu usage, and ram usage

Make sure to fill in your own Twitter keys!!


To create a cron job to auto execute:

1)From terminal execute: $sudo crontab -e

2)Add a cron job at the bottom of the file.

Example (tweets a status every 60 mins): */60 * * * * python /home/pi/status.py

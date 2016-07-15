#!/usr/bin/env python
#Max Abrams 2016
#status.py - Simple python program demonstrating the twitter api. When ran, this will tweet cpu temp, free disk space, cpu usage, and ram usage
#Make sure to use your own Twitter keys!!

import sys
import os
from twython import Twython

#Read CPU Temp
line = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline().strip()
temp = line.split('=')[1].split("'")[0]
temp = float(temp) * 9.0 / 5.0 + 32 #Convert to F
temp = str(temp) #Convert to string

#Read Free Disk Space
disks = os.popen("df -h /")
line = disks.readline()
line = disks.readline()
space = line.split()[2] #Index 2 is remaining

#Read CPU Usage
percent = (str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

#Read RAM Usage
ram = os.popen('free')
line = ram.readline()
line = ram.readline()
ram = line.split()[2]

#Post to Twitter
CONSUMER_KEY = '___YOUR_CONSUMER_KEY___'
CONSUMER_SECRET = '___YOUR_CONSUMER_SECRET___'
ACCESS_KEY = '___YOUR_ACCESS_KEY___'
ACCESS_SECRET = '___YOUR_ACCESS_SECRET___'

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET) 

api.update_status(status='Temp(F): ' + temp + ', Free Space: ' + space + ', CPU(%): ' + percent + ', RAM: ' + ram + ', Auto #Cluster Status')

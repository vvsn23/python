#!/bin/sh



ip=`cat /var/www/html/port4.txt`
port=`cat /var/www/html/port51.txt`
#baudrate=`cat /`
#echo "$ip"
#echo "$port"

baudrate1=`cat /var/www/html/port2.txt`
#echo "$baudrate"
baudrate=${baudrate1%%,*}
#echo "$baudrate"


sudo python /home/lemaker/satya.py --parity N -c $ip:$port /dev/ttyS0 $baudrate

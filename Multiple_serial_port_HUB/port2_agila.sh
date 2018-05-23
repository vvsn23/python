#!/bin/sh



ip=`cat /var/www/html/port4.txt`
port=`cat /var/www/html/port51.txt`
#echo "$ip"
#echo "$port"

baudrate1=`cat /var/www/html/port2.txt`
baudrate=${baudrate1%%,*}


sudo python /home/lemaker/port2_agila.py --parity N -c $ip:$port /dev/ttyS0 $baudrate

#!/bin/sh
ip=`cat /var/www/html/port4.txt`
port=`cat /var/www/html/port52.txt`
#baudrate=`cat /`
#echo "$ip"
#echo "$port"

baudrate1=`cat /var/www/html/port3.txt`
#echo "$baudrate"
baudrate=${baudrate1%%,*}
#echo "$baudrate"


sudo python /home/lemaker/satya3.py --parity N -c $ip:$port /dev/ttyS5 $baudrate

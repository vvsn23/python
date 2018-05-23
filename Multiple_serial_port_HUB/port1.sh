#!/bin/sh
ip=`cat /var/www/html/port4.txt`
port=`cat /var/www/html/port5.txt`

baudrate1=`cat /var/www/html/port3.txt`
baudrate=${baudrate1%%,*}


sudo python /home/lemaker/port1.py --parity N -c $ip:$port /dev/ttyS2 $baudrate

#!/bin/bash
echo 47 > /sys/class/gpio/export 
sudo echo in > /sys/class/gpio/gpio47/direction 

while true; 
do
        $(sudo cat /sys/class/gpio/gpio47/value > /home/lemaker/reset.txt)
        value=`cat /home/lemaker/reset.txt`
        if [ $value -eq 0 ]
                then
                 sudo sh /home/lemaker/Switch/sw_re.sh
                 sleep 1
        fi
        if [ $value -eq 1 ]
	then
                 cd /
                 cd /home/lemaker/Switch
                 $(sudo cp 2.txt b.txt)
                 cd /
                sleep 1
        fi 
done

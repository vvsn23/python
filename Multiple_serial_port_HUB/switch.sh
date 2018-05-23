#!/bin/sh
echo 47 > /sys/class/gpio/export
sudo echo in > /sys/class/gpio/gpio47/direction


while true;
do
        $(sudo cat /sys/class/gpio/gpio47/value > /home/lemaker/reset.txt)
        value=`cat /home/lemaker/reset.txt`
        if [ $value -eq 0 ]
                then
                 echo 'switch is on-state'
		 

        fi
        if [ $value -eq 1 ]
        then
                echo "switch is off-state"
        fi
done

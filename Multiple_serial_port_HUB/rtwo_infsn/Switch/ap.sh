#!/bin/bash

sudo ifdown wlan2
sleep 1
sudo killall hostapd
sleep 2
sudo ifdown eth0
sleep 1
sudo service network-manager restart
sleep 3

sudo cp /home/lemaker/ap /etc/network/interfaces
sleep 1
sudo udhcpd /etc/udhcpd.conf
sleep 2
sudo hostapd -B /etc/hostapd/hostapd.conf
sleep 3
sudo service network-manager restart
sleep 3
sudo ifup p2p0
sleep 1
#sudo reboot now

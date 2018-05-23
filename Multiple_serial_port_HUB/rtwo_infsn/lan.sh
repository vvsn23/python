#!/bin/sh


sudo killall hostapd
sleep 2
sudo ifdown p2p0
sleep 1
sudo ifdown wlan2
sleep 1
sudo service network-manager restart
sleep 3

sudo cp /var/www/html/static_lan.txt /etc/network/interfaces
sleep 2
sudo service network-manager restart
sleep 3
sudo ifdown p2p0
sudo ifup eth0
sleep 1
sudo ifconfig eth0 up
sleep 2


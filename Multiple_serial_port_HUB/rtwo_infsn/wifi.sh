#!/bin/sh

sudo killall hostapd
sleep 3
sudo cp /var/www/html/static_wi.txt  /etc/network/interfaces
sleep 1
sudo ifconfig p2p0 down
sleep 1
sudo ifup wlan2
sleep 1
sudo service network-manager restart
sleep 3
sudo ifdown wlan2
sudo ifdown p2p0
sleep 2
sudo ifup wlan2
sleep 2

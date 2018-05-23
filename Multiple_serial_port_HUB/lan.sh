#!/bin/sh

sudo ifdown --force wlan1
sudo sleep 2
sudo cp /var/www/html/static_lan.txt /etc/network/interfaces
sudo sleep 3
sudo service networking restart
sudo sleep 10
sudo ifup --force  eth0
sleep 5
sudo killall hostapd
sleep 2
sudo ifdown --force p2p0
sleep 2


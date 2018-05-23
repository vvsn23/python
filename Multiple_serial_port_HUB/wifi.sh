#!/bin/sh

sudo modprobe wlan_8723bs
sudo sleep 1
sudo ifdown --force eth0
sudo sleep 2
sudo cp /var/www/html/static_wi.txt /etc/network/interfaces
sudo sleep 2
sudo service networking restart
sudo sleep 3
sudo ifdown --force wlan1
sudo sleep 2
sudo ifup --force wlan1
sudo sleep 5
sudo killall hostapd
sudo sleep 2
sudo ifdown --force p2p0
sudo sleep 2

#!/bin/sh

sudo killall hostapd
sudo sleep 3
sudo killall wpa_supplicant
sudo sleep 1
sudo cp /home/lemaker/ap /etc/network/interfaces
sudo sleep 1
sudo service networking restart
sudo sleep 1
sudo udhcpd /etc/udhcpd.conf
sudo sleep 1
sudo hostapd -B /etc/hostapd/hostapd.conf
sudo sleep 1
sudo service network-manager restart
sudo sleep 1
sudo ifdown --force  wlan1
sudo sleep 1
sudo ifup --force  p2p0
sudo sleep 1
sudo udhcpd /etc/udhcpd.conf
sudo sleep 1
sudo hostapd -B /etc/hostapd/hostapd.conf
sudo sleep 1


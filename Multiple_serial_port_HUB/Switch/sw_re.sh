#!/bin/sh
sudo cp /var/www/html/net_t.txt /var/www/html/net.txt
sudo cp /var/www/html/port11.txt /var/www/html/port1.txt  
sudo cp /var/www/html/port22.txt /var/www/html/port2.txt
sleep 1
sudo cp /var/www/html/port31.txt /var/www/html/port3.txt  
sudo cp /var/www/html/port41.txt /var/www/html/port4.txt 
sudo cp /var/www/html/port555.txt /var/www/html/port5.txt 
sudo cp /var/www/html/port511.txt /var/www/html/port51.txt 
sleep 1
sudo cp /var/www/html/port521.txt /var/www/html/port52.txt
sudo cp /var/www/html/portu1.txt /var/www/html/portu.txt 
sudo cp /var/www/html/portp1.txt /var/www/html/portp.txt 
sleep 1
sudo cp /var/www/html/portw11.txt /var/www/html/portw1.txt
sudo cp /var/www/html/portw21.txt /var/www/html/portw2.txt
sudo cp /var/www/html/portw31.txt /var/www/html/portw3.txt 
sleep 1
sudo sh /home/lemaker/Switch/ap.sh
sleep 10

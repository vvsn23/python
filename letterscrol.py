#!/usr/bin/python

import os, time

x = "\n\n\n\n\n\n\n\n\n\t\t\t HARE KRISHNA HARE KRISHNA \n\t\t\t KRISHNA KRISHNA HARE HARE \n\t\t\t HARE RAMA HARE RAMA  \n\t\t\t RAMA RAMA HARE HARE "
z=0
y=1

while y==1:
	while z <= len(x) :
		os.system("clear") 
		print x[:z]
		time.sleep(.05)
		z= z+1
	time.sleep(2)
	os.system("clear")
	z=0
#raw_input("Press Enter To Quit!")

import os
import sys
import time

import subprocess
from time import sleep

#b = open('/home/re/auto/naddfiles/Result.csv', 'a')
#a = b.write(b)
aa3 = open('/var/www/html/result2.txt', 'w')
bb3 = aa3.write('1')
aa3.close()
ff2=open("/var/www/html/result2.txt", "r")
a2=ff2.read()
a22 = int(a2)
#time.sleep(2)
print a2

ff2.close()

while 1:

	ff11=open("/var/www/html/net.txt", "r")
	a1=ff11.read()	
	a11 = str(a1)
#	print a11
        ff11.close()
	ff2=open("/var/www/html/result2.txt", "r")
	a2=ff2.read()
	a22 = int(a2)
	time.sleep(2)
	print a22
	ff2.close()
	if a11 == 'WIFI(CLIENT)-SERIAL' and a22 == 1:
    		print "WIFI(CLIENT)-SERIAL" 

    		aa1 = open('/var/www/html/result2.txt', 'w')
    	
		bb3 = aa1.write('2')
		aa1.close()

		import subprocess
		from time import sleep
		subprocess.Popen(["sh",'wifi.sh'])
		sleep(20)
                print "WIFI(CLIENT)-SERIAL"

			
	if a11 == 'ETHERNET-SERIAL' and a22 == 1:


                print "ETHERNET-SERIAL"

                import subprocess
                from time import sleep
                subprocess.Popen(["sh",'lan.sh'])
                sleep(10)

                aa2 = open('/var/www/html/result2.txt', 'w')

                
		bb3 = aa2.write('2')
		aa2.close()
    		
	if a11 == 'WIFI(AP)-SERIAL' and a22 == 1:

                import subprocess
                from time import sleep
		sleep(3)
                subprocess.Popen(["sh",'/home/lemaker/Switch/ap.sh'])
                sleep(15)

		aa3 = open('/var/www/html/result2.txt', 'w')
		
		bb3 = aa3.write('2')
		aa3.close()
    		print "WIFI(AP)-SERIAL"

	else :
    		print "nnnnnnnnooooooooo"


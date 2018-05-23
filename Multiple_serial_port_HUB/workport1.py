
import serial
import time
import datetime
import time
import os
import socket
import sys

ff1 = open("/var/www/html/port4.txt", "r")
buff1 = ff1.read()
ff1.close()
ff2 = open("/var/www/html/port5.txt", "r")
buff2 = ff2.read()
gu= int(buff2)
ff2.close()
#print buff1
#print gu
time.sleep(0.8)
c =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = c.connect_ex((buff1, gu))

#print result

while 1:

        while 1:
                text_file = open("/var/www/html/port1.txt", "r")
                buff = text_file.read()
                words = buff.split(",")
                r1= words[0]
                r2= int(words[1])
                port = serial.Serial(
                        port = '/dev/ttyS2',
                        baudrate = r1,
			parity=serial.PARITY_EVEN,
                        stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS,
                        timeout= 0,
                        rtscts = True
                )
                rcv0=port.read(2048)
		
#                print(rcv0)
#                print  "loop"
                if result == 1:

                        ff1 = open("/var/www/html/port4.txt", "r")
                        buff1 = ff1.read()
                        ff1.close()
                        ff2 = open("/var/www/html/port5.txt", "r")
                        buff2 = ff2.read()
                        gu=int(buff2)
                        ff2.close()

			try:
				c =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = c.connect_ex((buff1, gu))
				ee=c.send(rcv0)
				#time.sleep(0.02)  
				try:
					c.setblocking(0)
					ee1=c.recv(2048)
					ee2=port.write(ee1)
				except socket.error:
					print "data"
				
				c.setblocking(1)	 	     
		
			except socket.error:
#	    			print('connection error1111111111')
	    		#	sys.exit(0)
     				result =1		
				break		
		

	    	if result == 0:
		
#			print result
#			print "everything it's ok!"
			
#			result = c.connect_ex((buff1, gu))
#			time.sleep(0.3)  
	 	     
			
			try:
	    		
				ee=c.send(rcv0)
#			        print ee
#				print rcv0
				try:
					c.setblocking(0)
					ee1=c.recv(2048)
					ee2=port.write(ee1)
					#print "satya"
					#print ee2
					if (ee2==0):
						c =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						result = c.connect_ex((buff1, gu))
				except socket.error:
					print "data1"
				c.setblocking(1)
					
			except socket.error:
#	    			print('connection error22222222')
				result = 1
	    			break
        


                else:

                       

                        ff1 = open("/var/www/html/port4.txt", "r")
                        buff1 = ff1.read()
                        ff1.close()
                        ff2 = open("/var/www/html/port5.txt", "r")
                        buff2 = ff2.read()
                        gu=int(buff2)
                        ff2.close()


                        try:
                                c =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                result = c.connect_ex((buff1, gu))
                                ee=c.send(rcv0)
                                #time.sleep(0.4)
				try:
					c.setblocking(0)
					ee1=c.recv(2048)
					ee2=port.write(ee1)
				except socket.error:
					print "data3"
				
				c.setblocking(1)

                        except socket.error:
#                                print('connection error1111111111')
                        #       sys.exit(0)
                                result =1
                                break


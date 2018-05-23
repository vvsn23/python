import serial
import time
import datetime
import time
import os
import socket

ff1 = open("/var/www/html/port4.txt", "r")
buff1 = ff1.read()
ff1.close()
ff2 = open("/var/www/html/port5.txt", "r")
buff2 = ff2.read()
gu=int(buff2)
ff2.close()
print buff1
print gu
c= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = buff1
ports = gu
print host
print ports
c.connect((host, ports))
ip1=huff1
po1=gu
while 1:

    ff11 = open("/var/www/html/port4.txt", "r")
    buff11 = ff11.read()
    ip2= buff11
    ff11.close()
    ff21 = open("/var/www/html/port5.txt", "r")
    buff22 = ff21.read()
    po2=int(buff22)
    ff21.close()
    if po1 != po2:
        c= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host1 = ip2
        ports1 = po2
        print host1
        print ports1
        c.connect((host1, ports1))
        print("ipip ")
        text_file = open("/var/www/html/port1.txt", "r")
        buff = text_file.read()
        words = buff.split(",")
        r1= words[0]
        r2= int(words[1])
        port = serial.Serial(
                port = '/dev/ttyUSB0',
                baudrate = 115200,
                bytesize = 8,
                timeout= 1,
                rtscts = True
        )
        rcv0=port.read(900)
        print(rcv0)
        c.send(rcv0)
c.close()

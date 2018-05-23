
import serial
import os
import time

port = serial.Serial(port='/dev/ttyS5', baudrate=115200, bytesize=8, timeout=1, rtscts=True)
text1='Royal Elegance Technologies\xfd'   # transmitting data
while 1:
	port.write(text1)
	time.sleep(5)
	rcv1 = port.read(600)   # receving typing from x-ctu from  windows
	time.sleep(5)
	print rcv1

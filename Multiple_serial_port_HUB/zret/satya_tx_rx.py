import serial
import time
import datetime
import time
import os
#port = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, bytesize=8)
port = serial.Serial(port='/dev/ttyS5', baudrate=115200, bytesize=8, timeout=1, rtscts=False)
text1='royal elegance technologies\xfd'   # transmitting data 
port.write(text1)
time.sleep(2)


rcv1 = port.read(600)   # receving typing from x-ctu from  windows
time.sleep(5)
print rcv1

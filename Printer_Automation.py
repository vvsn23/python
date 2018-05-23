# USB Printer Automation by VVSN
# Automatic comport detection and pygtk GUI method
#
# sending the respected data to the printer
#
# user: V V Sataynarayana Thorati 
###########################################################
import pygtk
pygtk.require('2.0')
import gtk
import signal
import time
import sys
import subprocess
from time import sleep
import pygtk
pygtk.require("2.0")
import gobject
import gtk
gtk.gdk.threads_init()
import threading
t1=0
t2=0
t3=0
t4=0
t5=0
usb='0'
class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        self.set_title("Printer Automation")    
        self.set_default_size(1900, 800)
	window=gtk.Window()
        fixed = gtk.Fixed()
	send=gtk.Button("                     				Printer Testing commands                	                   ")
        fixed.put(send, 700, 20)

	send1=gtk.Label("Font_1_select:")
        fixed.put(send1, 70, 70)
	send1=gtk.Label("1.")
        fixed.put(send1, 45, 70)
	entry1 = gtk.Entry()
        fixed.put(entry1, 200, 70)
	send1=gtk.Button("SEND")
	send1.connect("clicked",self.send_press, entry1, '1')
        fixed.put(send1, 400, 70)

	send2=gtk.Label("Font_2_select:")
        fixed.put(send2, 70, 100)
	send1=gtk.Label("2.")
        fixed.put(send1, 45, 100)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 100)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '2')
        fixed.put(send2, 400, 100)

	send2=gtk.Label("Left_Alignment:")
        fixed.put(send2, 70, 130)
	send1=gtk.Label("3.")
        fixed.put(send1, 45, 130)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 130)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '3')
        fixed.put(send2, 400, 130)

	send2=gtk.Label("Center_Alignment:")
        fixed.put(send2, 70, 160)
	send1=gtk.Label("4.")
        fixed.put(send1, 45, 160)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 160)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '4')
        fixed.put(send2, 400, 160)

	send2=gtk.Label("Right_Alignment:")
        fixed.put(send2, 70, 190)
	send1=gtk.Label("5.")
        fixed.put(send1, 45, 190)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 190)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '5')
        fixed.put(send2, 400, 190)

	send2=gtk.Label("No_line_Feed:")
        fixed.put(send2, 70, 220)
	send1=gtk.Label("6.")
        fixed.put(send1, 45, 220)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 220)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '6')
        fixed.put(send2, 400, 220)

	send2=gtk.Label("F1_Without_Feed:")
        fixed.put(send2, 70, 250)
	send1=gtk.Label("7.")
        fixed.put(send1, 45, 250)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 250)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '7')
        fixed.put(send2, 400, 250)

	send2=gtk.Label("F2_Without_Feed")
        fixed.put(send2, 70, 280)
	send1=gtk.Label("8.")
        fixed.put(send1, 45, 280)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 280)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '8')
        fixed.put(send2, 400, 280)

	send2=gtk.Label("F1_Left_WoF:")
        fixed.put(send2, 70, 310)
	send1=gtk.Label("9.")
        fixed.put(send1, 45, 310)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 310)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '9')
        fixed.put(send2, 400, 310)

	send2=gtk.Label("F1_Center_WoF:")
        fixed.put(send2, 70, 340)
	send1=gtk.Label("10.")
        fixed.put(send1, 45, 340)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 340)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '10')
        fixed.put(send2, 400, 340)

	send1=gtk.Label("F1_Right_WoF:")
        fixed.put(send1, 70, 370)
	send1=gtk.Label("11.")
        fixed.put(send1, 45, 370)
	entry1 = gtk.Entry()
        fixed.put(entry1, 200, 370)
	send1=gtk.Button("SEND")
	send1.connect("clicked",self.send_press, entry1, '11')
        fixed.put(send1, 400, 370)

	send2=gtk.Label("F2_Left_WOF")
        fixed.put(send2, 70, 400)
	send1=gtk.Label("12.")
        fixed.put(send1, 45, 400)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 400)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '12')
        fixed.put(send2, 400, 400)

	send2=gtk.Label("F2_Center_WOF:")
        fixed.put(send2, 70, 430)
	send1=gtk.Label("13.")
        fixed.put(send1, 45, 430)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 430)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '13')
        fixed.put(send2, 400, 430)

	send2=gtk.Label("F2_Right_WOF")
        fixed.put(send2, 70, 460)
	send1=gtk.Label("14.")
        fixed.put(send1, 45, 460)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 460)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '14')
        fixed.put(send2, 400, 460)

	send2=gtk.Label("F1_NL_2ndData:")
        fixed.put(send2, 70, 490)
	send1=gtk.Label("15.")
        fixed.put(send1, 45, 490)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 490)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '15')
        fixed.put(send2, 400, 490)

	send2=gtk.Label("F2_NL_2ndData")
        fixed.put(send2, 70, 520)
	send1=gtk.Label("16.")
        fixed.put(send1, 45, 520)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 520)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '16')
        fixed.put(send2, 400, 520)

	send2=gtk.Label("HBarcode_EAN_8:")
        fixed.put(send2, 70, 550)
	send1=gtk.Label("17.")
        fixed.put(send1, 45, 550)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 550)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '17')
        fixed.put(send2, 400, 550)

	send2=gtk.Label("HBarcode_UPC:")
        fixed.put(send2, 70, 580)
	send1=gtk.Label("18.")
        fixed.put(send1, 45, 580)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 580)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '18')
        fixed.put(send2, 400, 580)

	send2=gtk.Label("HBarcode_128:")
        fixed.put(send2, 70, 610)
	send1=gtk.Label("19.")
        fixed.put(send1, 45, 610)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 610)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '19')
        fixed.put(send2, 400, 610)

	send2=gtk.Label("HBarcode_39:")
        fixed.put(send2, 70, 640)
	send1=gtk.Label("20.")
        fixed.put(send1, 45, 640)
	entry2 = gtk.Entry()
        fixed.put(entry2, 200, 640)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '20')
        fixed.put(send2, 400, 640)




	send1=gtk.Label("HBarcode_I2of5:")
        fixed.put(send1, 520, 70)
	send1=gtk.Label("21.")
        fixed.put(send1, 500, 70)
	entry1 = gtk.Entry()
        fixed.put(entry1, 650, 70)
	send1=gtk.Button("SEND")
	send1.connect("clicked",self.send_press, entry1, '21')
        fixed.put(send1, 850, 70)

	send2=gtk.Label("VBarcode_EAN_8:")
        fixed.put(send2, 520, 100)
	send1=gtk.Label("22.")
        fixed.put(send1, 500, 100)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 100)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '22')
        fixed.put(send2, 850, 100)

	send2=gtk.Label("VBarcode_UPC:")
        fixed.put(send2, 520, 130)
	send1=gtk.Label("23.")
        fixed.put(send1, 500, 130)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 130)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '23')
        fixed.put(send2, 850, 130)

	send2=gtk.Label("VBarcode_128:")
        fixed.put(send2, 520, 160)
	send1=gtk.Label("24.")
        fixed.put(send1, 500, 160)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 160)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '24')
        fixed.put(send2, 850, 160)

	send2=gtk.Label("VBarcode_39:")
        fixed.put(send2, 520, 190)
	send1=gtk.Label("25.")
        fixed.put(send1, 500, 190)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 190)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '25')
        fixed.put(send2, 850, 190)

	send2=gtk.Label("VBarcode_I2of5:")
        fixed.put(send2, 520, 220)
	send1=gtk.Label("26.")
        fixed.put(send1, 500, 220)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 220)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '26')
        fixed.put(send2, 850, 220)

	send2=gtk.Label("Uplo_Tamplate1:")
        fixed.put(send2, 520, 250)
	send1=gtk.Label("27.")
        fixed.put(send1, 500, 250)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 250)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '27')
        fixed.put(send2, 850, 250)
	send2=gtk.Label("Uplo_Tamplate2")
        fixed.put(send2, 520, 280)
	send1=gtk.Label("28.")
        fixed.put(send1, 500, 280)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 280)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '28')
        fixed.put(send2, 850, 280)
	send2=gtk.Label("Uplo_Tamplate3:")
        fixed.put(send2, 520, 310)
	send1=gtk.Label("29.")
        fixed.put(send1, 500, 310)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 310)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '29')
        fixed.put(send2, 850, 310)
	send2=gtk.Label("Uplo_Tamplate4:")
        fixed.put(send2, 520, 340)
	send1=gtk.Label("30.")
        fixed.put(send1, 500, 340)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 340)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '30')
        fixed.put(send2, 850, 340)
	send1=gtk.Label("Uplo_Tamplate5:")
        fixed.put(send1, 520, 370)
	send1=gtk.Label("31.")
        fixed.put(send1, 500, 370)
	entry11 = gtk.Entry()
        fixed.put(entry11, 650, 370)
	send1=gtk.Button("SEND")
	send1.connect("clicked",self.send_press, entry11, '31')
        fixed.put(send1, 850, 370)
	send2=gtk.Label("P_Tamplate1:")
        fixed.put(send2, 520, 400)
	send1=gtk.Label("32.")
        fixed.put(send1, 500, 400)
	entry12 = gtk.Entry()
        fixed.put(entry12, 650, 400)
	send2=gtk.Button("READT1")
	send2.connect("clicked",self.send_press, entry12, '32')
        fixed.put(send2, 850, 400)
	send2=gtk.Label("P_Tamplate2:")
        fixed.put(send2, 520, 430)
	send1=gtk.Label("33.")
        fixed.put(send1, 500, 430)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 430)
	send2=gtk.Button("READT2")
	send2.connect("clicked",self.send_press, entry2, '33')
        fixed.put(send2, 850, 430)
	send2=gtk.Label("P_Tamplate3:")
        fixed.put(send2, 520, 460)
	send1=gtk.Label("34.")
        fixed.put(send1, 500, 460)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 460)
	send2=gtk.Button("READT3")
	send2.connect("clicked",self.send_press, entry2, '34')
        fixed.put(send2, 850, 460)
	send2=gtk.Label("P_Tamplate4:")
        fixed.put(send2, 520, 490)
	send1=gtk.Label("35.")
        fixed.put(send1, 500, 490)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 490)
	send2=gtk.Button("READT4")
	send2.connect("clicked",self.send_press, entry2, '35')
        fixed.put(send2, 850, 490)
	send2=gtk.Label("P_Tamplate5:")
        fixed.put(send2, 520, 520)
	send1=gtk.Label("36.")
        fixed.put(send1, 500, 520)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 520)
	send2=gtk.Button("READT5")
	send2.connect("clicked",self.send_press, entry2, '36')
        fixed.put(send2, 850, 520)
	send2=gtk.Label("Line_by_line:")
        fixed.put(send2, 520, 550)
	send1=gtk.Label("37.")
        fixed.put(send1, 500, 550)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 550)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '37')
        fixed.put(send2, 850, 550)
	send2=gtk.Label("Line_pich_LEV-15:")
        fixed.put(send2, 520, 580)
	send1=gtk.Label("38.")
        fixed.put(send1, 500, 580)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 580)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '38')
        fixed.put(send2, 850, 580)



	send2=gtk.Label("Backword_feed:")
        fixed.put(send2, 520, 610)
	send1=gtk.Label("39.")
        fixed.put(send1, 500, 610)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 610)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '39')
        fixed.put(send2, 850, 610)

	send2=gtk.Label("Text_file_path:")
        fixed.put(send2, 520, 640)
	send1=gtk.Label("40.")
        fixed.put(send1, 500, 640)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 640)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '40')
        fixed.put(send2, 850, 640)





	send1=gtk.Label("41.")
        fixed.put(send1, 950, 70)
	send2=gtk.Label("Black-white_Select:")
        fixed.put(send2, 970, 70)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 70)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '41')
        fixed.put(send2, 1300, 70)
	send1=gtk.Label("42.")
        fixed.put(send1, 950, 100)
	send2=gtk.Label("Black-white_Cancel:")
        fixed.put(send2, 970, 100)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 100)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '42')
        fixed.put(send2, 1300, 100)
	send1=gtk.Label("43.")
        fixed.put(send1, 950, 130)
	send2=gtk.Label("LineSpace01select:")
        fixed.put(send2, 970, 130)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 130)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '43')
        fixed.put(send2, 1300, 130)
	send1=gtk.Label("44.")
        fixed.put(send1, 950, 160)
	send2=gtk.Label("Li_Space_05_select:")
        fixed.put(send2, 970, 160)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 160)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '44')
        fixed.put(send2, 1300, 160)
	send1=gtk.Label("45.")
        fixed.put(send1, 950, 190)
	send2=gtk.Label("Line_Space_cancel:")
        fixed.put(send2, 970, 190)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 190)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '45')
        fixed.put(send2, 1300, 190)
	send1=gtk.Label("46.")
        fixed.put(send1, 950, 220)
	send2=gtk.Label("One_by_Six_pitch:")
        fixed.put(send2, 970, 220)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 220)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '46')
        fixed.put(send2, 1300, 220)
	send1=gtk.Label("47.")
        fixed.put(send1, 950, 250)
	send2=gtk.Label("One_by_six_cancal:")
        fixed.put(send2, 970, 250)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 250)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '47')
        fixed.put(send2, 1300, 250)
	send1=gtk.Label("48.")
        fixed.put(send1, 950, 280)
	send2=gtk.Label("Lev-1-Print_Mode:")
        fixed.put(send2, 970, 280)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 280)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '48')
        fixed.put(send2, 1300, 280)
	send1=gtk.Label("49.")
        fixed.put(send1, 950, 310)
	send2=gtk.Label("Lev-1-Print_Mode:")
        fixed.put(send2, 970, 310)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 310)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '49')
        fixed.put(send2, 1300, 310)
	send1=gtk.Label("50.")
        fixed.put(send1, 950, 340)
	send2=gtk.Label("Lev-3-Print_Mode:")
        fixed.put(send2, 970, 340)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 340)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '50')
        fixed.put(send2, 1300, 340)




	send1=gtk.Label("51.")
        fixed.put(send1, 950, 370)
	send2=gtk.Label("Printer_Quality_L1:")
        fixed.put(send2, 970, 370)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 370)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '51')
        fixed.put(send2, 1300, 370)
	send1=gtk.Label("52.")
        fixed.put(send1, 950, 400)
	send2=gtk.Label("Printer_Quality_L2:")
        fixed.put(send2, 970, 400)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 400)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '52')
        fixed.put(send2, 1300, 400)
	send1=gtk.Label("53.")
        fixed.put(send1, 950, 430)
	send2=gtk.Label("Hrz_tab_posit-12:")
        fixed.put(send2, 970, 430)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 430)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '53')
        fixed.put(send2, 1300, 430)
	send1=gtk.Label("54.")
        fixed.put(send1, 950, 460)
	send2=gtk.Label("V-Loc-Select_default:")
        fixed.put(send2, 970, 460)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 460)
	send2=gtk.Button("READ-I")
	send2.connect("clicked",self.send_press, entry2, '54')
        fixed.put(send2, 1300, 460)
	send1=gtk.Label("55.")
        fixed.put(send1, 950, 490)
	send2=gtk.Label("F1-selected-default:")
        fixed.put(send2, 970, 490)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 490)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '55')
        fixed.put(send2, 1300, 490)
	send1=gtk.Label("56.")
        fixed.put(send1, 950, 520)
	send2=gtk.Label("F2-selected-default:")
        fixed.put(send2, 970, 520)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 520)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '56')
        fixed.put(send2, 1300, 520)
	send1=gtk.Label("57.")
        fixed.put(send1, 950, 550)
	send2=gtk.Label("Serial-Device-status")
        fixed.put(send2, 970, 550)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 550)
	send2=gtk.Button("READ-PS")
	send2.connect("clicked",self.send_press, entry2, '57')
        fixed.put(send2, 1300, 550)
	send1=gtk.Label("58.")
        fixed.put(send1, 950, 580)
	send2=gtk.Label("Page Length-19:")
        fixed.put(send2, 970, 580)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 580)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '58')
        fixed.put(send2, 1300, 580)
	send1=gtk.Label("59.")
        fixed.put(send1, 950, 610)
	send2=gtk.Label("90 Drgree Select:")
        fixed.put(send2, 970, 610)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 610)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '59')
        fixed.put(send2, 1300, 610)
	send1=gtk.Label("60.")
        fixed.put(send1, 950, 640)
	send2=gtk.Label("90 Degree Cancel:")
        fixed.put(send2, 970, 640)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1110, 640)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '60')
        fixed.put(send2, 1300, 640)

	send1=gtk.Label("61.")
        fixed.put(send1, 1400, 70)
	send2=gtk.Label("Battery&N0.prints:")
        fixed.put(send2, 1420, 70)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1570, 70)
	send2=gtk.Button("READ_B")
	send2.connect("clicked",self.send_press, entry2, '61')
        fixed.put(send2, 1760, 70)
	send1=gtk.Label("62.")
        fixed.put(send1, 1400, 100)
	send2=gtk.Label("B_Serial_img_Path:")
        fixed.put(send2, 1420, 100)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1570, 100)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '62')
        fixed.put(send2, 1760, 100)
	send1=gtk.Label("63.")
        fixed.put(send1, 1400, 130)
	send2=gtk.Label("A_Serial_img_Path:")
        fixed.put(send2, 1420, 130)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1570, 130)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press, entry2, '63')
        fixed.put(send2, 1760, 130)


	send1=gtk.Label("64.")
        fixed.put(send1, 1400, 160)
	send2=gtk.Label("A_upld_img_Path_V:")
        fixed.put(send2, 1420, 160)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1570, 160)
	send2=gtk.Button("UPLD_V")
	send2.connect("clicked",self.send_press, entry2, '64')
        fixed.put(send2, 1760, 160)
	send1=gtk.Label("65.")
        fixed.put(send1, 1400, 190)
	send2=gtk.Label("A_upld_img_Path_W:")
        fixed.put(send2, 1420, 190)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1570, 190)
	send2=gtk.Button("UPLD_W")
	send2.connect("clicked",self.send_press, entry2, '65')
        fixed.put(send2, 1760, 190)


	send1=gtk.Label("66.")
        fixed.put(send1, 1400, 220)
	send2=gtk.Label("A_print_img_Vloc:")
        fixed.put(send2, 1420, 220)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1570, 220)
	send2=gtk.Button("READV")
	send2.connect("clicked",self.send_press, entry2, '66')
        fixed.put(send2, 1760, 220)
	send1=gtk.Label("67.")
        fixed.put(send1, 1400, 250)
	send2=gtk.Label("A_print_img_Wloc:")
        fixed.put(send2, 1420, 250)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1570, 250)
	send2=gtk.Button("READW")
	send2.connect("clicked",self.send_press, entry2, '67')
        fixed.put(send2, 1760, 250)
	send1=gtk.Label("68.")
        fixed.put(send1, 1400, 280)
	send2=gtk.Label("A_print_img_Xloc:")
        fixed.put(send2, 1420, 280)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1570, 280)
	send2=gtk.Button("READX")
	send2.connect("clicked",self.send_press, entry2, '68')
        fixed.put(send2, 1760, 280)



	send1=gtk.Label("69.")
        fixed.put(send1, 1400, 310)
	send2=gtk.Label("A_Earse_img_Vloc:")
        fixed.put(send2, 1420, 310)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1570, 310)
	send2=gtk.Button("EARSEV")
	send2.connect("clicked",self.send_press, entry2, '69')
        fixed.put(send2, 1760, 310)
	send1=gtk.Label("70.")
        fixed.put(send1, 1400, 340)
	send2=gtk.Label("A_Earse_img_Wloc:")
        fixed.put(send2, 1420, 340)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1570, 340)
	send2=gtk.Button("EARSEW")
	send2.connect("clicked",self.send_press, entry2, '70')
        fixed.put(send2, 1760, 340)




	send1=gtk.Label("71.")
        fixed.put(send1, 1400, 370)
	send2=gtk.Label("png-jpeg/jpg:")
        fixed.put(send2, 1420, 370)
	entry2 = gtk.Entry()
        fixed.put(entry2, 1570, 370)
	send2=gtk.Button("img-print")
	send2.connect("clicked",self.send_press, entry2, '71')
        fixed.put(send2, 1760, 370)


	send2=gtk.Label("usb_setting:")
        fixed.put(send2, 550, 700)
	entry2 = gtk.Entry()
        fixed.put(entry2, 650, 700)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press1, entry2, '400')
        fixed.put(send2, 840, 700)
	send2=gtk.Label("m_usb_setting:")
        fixed.put(send2, 120, 700)
	entry2 = gtk.Entry()
        fixed.put(entry2, 250, 700)
	send2=gtk.Button("SEND")
	send2.connect("clicked",self.send_press4, entry2, '402')
        fixed.put(send2, 440, 700)




        self.connect("destroy", gtk.main_quit)
        self.add(fixed)
        self.show_all()


    def on_clicked(self, widget, data=None):
	A = str(data)
        B = str(widget.get_active())
        rr=A + B
        print rr
    def send_press4(self, widget, entry, data=None):
	global usb
	a = str(data)
	usb = entry.get_text()
	print usb
	import serial
	import time
	import datetime
	import os
	i=datetime.datetime.now()
	c1='/dev/'
	c2=usb
	cc= c1 + c2
	port = serial.Serial(port=cc, baudrate=115200, bytesize=8, timeout=1, rtscts=True)
	#port.write("dvds")
	if a=='402':
		a = '\x1b1'
		b="Printer is ready"
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	

    def send_press1(self, widget, entry, data=None):
	global usb

	a = str(data)
	usb = entry.get_text()	
	import os
	import subprocess
	cmd ="dmesg | grep tty | tail -1"
	p1 = subprocess.check_output(cmd, shell=True)
	p2 = p1.split()
	print p2[4]

	usb1= p2[4]
	usbl= usb1[0] + usb1[1] 
	print usb1
	print usbl

	if usbl == 'tt':
		p = subprocess.check_output(cmd, shell=True)
		usb2= usb1[0] + usb1[1] + usb1[2] + usb1[3] + usb1[4] + usb1[5] + usb1[6]
		print usb2
		c1='/dev/'
		c2=usb2
		usb= usb2
		cc= c1 + c2
		print cc
		import time	
		import serial
		port = serial.Serial(port=cc, baudrate=115200, bytesize=8, timeout=1, rtscts=True)	
		bq="Printer Ready"
		cq='\xfd'
		dq= bq + cq
		port.write(dq)
		rcva = port.read(900)
		print(rcva) 
		num=entry.get_text()
		pnum=widget.get_label()
		entry.set_text(usb)

	if usbl == 'pl':
		c1='/dev/'
		c2=p2[9]
		usb= c2
		cc= c1 + c2
		print cc
		import time
	
		import serial
		port = serial.Serial(port=cc, baudrate=115200, bytesize=8, timeout=1, rtscts=True)	
		bq="Printer Ready"
		cq='\xfd'
		dq= bq + cq
		port.write(dq)
		rcva = port.read(900)
		print(rcva)
		num=entry.get_text()
		pnum=widget.get_label()
		entry.set_text(usb) 


		
	if usb1 == 'cp210x' :
		c1='/dev/'
		c2=p2[9]
		usb= c2
		cc= c1 + c2
		print cc
		import time
	
		import serial
		port = serial.Serial(port=cc, baudrate=115200, bytesize=8, timeout=1, rtscts=True)	
		bq="Printer Ready"
		cq='\xfd'
		dq= bq + cq
		port.write(dq)
		rcva = port.read(900)
		print(rcva)
		num=entry.get_text()
		pnum=widget.get_label()
		entry.set_text(usb) 

	if usb1 == 'USB':
		p1 = subprocess.check_output(cmd, shell=True)
		p2 = p1.split()
		print p2[3]
		usb1=p2[3]
		usb2= usb1[0] + usb1[1] + usb1[2] + usb1[3] + usb1[4] + usb1[5] + usb1[6]
		print usb2
		c1='/dev/'
		c2=usb2
		usb= usb2
		cc= c1 + c2
		print cc
		import time	
		import serial
		port = serial.Serial(port=cc, baudrate=115200, bytesize=8, timeout=1, rtscts=True)	
		bq="Printer Ready"
		cq='\xfd'
		dq= bq + cq
		port.write(dq)
		rcva = port.read(900)
		print(rcva) 
		num=entry.get_text()
		pnum=widget.get_label()
		entry.set_text(usb)
		
	if usb1 == 'converter' :
		c1='/dev/'
		c2=p2[8]
		usb= c2
		cc= c1 + c2
		print cc
		import time
	
		import serial
		port = serial.Serial(port=cc, baudrate=115200, bytesize=8, timeout=1, rtscts=True)	
		bq="Printer Ready"
		cq='\xfd'
		dq= bq + cq
		port.write(dq)
		rcva = port.read(900)
		print(rcva)
		num=entry.get_text()
		pnum=widget.get_label()
		entry.set_text(usb) 

    def send_press(self, widget, entry, data=None):
	a = str(data)
      #  B = str(widget.get_active())
   	
        print a
	p = entry.get_text()
	print "Printting_Data " + p
	import serial
	import time
	import datetime
	import os
	i=datetime.datetime.now()
	c1='/dev/'
	c2=usb
	cc= c1 + c2
	port = serial.Serial(port=cc, baudrate=115200, bytesize=8, timeout=1, rtscts=True)
	#port.write("dvds")
	if a=='1':
		a = '\x1b1'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='2':
		a = '\x1b2'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='3':
		a = '\x1b5'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='4':
		a = '\x1b6'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='5':
		a = '\x1b7'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='6':
		a = '\x1b*'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='7':

		a = '\x1b1'
		b=p
		c='\x1b*\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='8':
		a = '\x1b2'
		b=p
		c='\x1b*\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='9':

		a = '\x1b1\x1b5'
		b=p
		c='\x1b*\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='10':
		a = '\x1b1\x1b6'
		b=p
		c='\x1b*\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='11':
		a = '\x1b1\x1b7'
		b=p
		c='\x1b*\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='12':
		a = '\x1b2\x1b5'
		b=p
		c='\x1b*\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='13':
		a = '\x1b2\x1b6'
		b=p
		c='\x1b*\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='14':
		a = '\x1b2\x1b7'
		b=p
		c='\x1b*\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='15':#$1b1Font1New_line_2nddata$1b*$fd
		a = '\x1b1'
		b=p
		c='\x1b*\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='16':#$1b2Font1New_line_2nddata$1b*$fd
		a = '\x1b2'
		b=p
		c='\x1b*\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='17':#$1b8)A08)C00101010$fd
		a = '\x1b8)A08)C0'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='18':#$1b8)A12)D146278490450$fd
		a = '\x1b8)A12)D'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='19':#$1b8)A08)ERoyaL5+2$fd
		a = '\x1b8)A808)E'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='20':#$1b8)A08)FROYAL990$fd
		a = '\x1B8)A08)F'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='21':#$1b8)A08)GROYAL990$fd
		a = '\x1b8)A08)G'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='22':#$1b8)B08)C00101010$fd
		a = '\x1b8)B08)C'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='23':#$1b8)B12)D146278490450$fd
		a = '\x1b8)B12)D'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='24':#$1b8)B08)ERoyaL5+2$fd
		a = '\x1b8)B08)E'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='25':#$1b8)B08)FROYAL990$fd
		a = '\x1b8)B08)F'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='26':#$1b8)B08)GROYAL990$fd
		a = '\x1b8)B08)G'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='27':#$1bU)T1009TEMPLATE1$fd
		global t1
		a = '\x1bU)T1009'
		b=p
		t1=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='28':#$1bU)T2009TEMPLATE2$fd
		global t2
		a = '\x1bU)T2009'
		b=p
		c='\xfd'
		t2=p
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='29':#$1bU)T3009TEMPLATE3$fd
		global t3

		a = '\x1bU)T3009'
		b=p
		t3=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='30':#$1bU)T4009TEMPLATE4$fd
		global t4
		a = '\x1bU)T4009'
		b=p
		c='\xfd'
		t4=p
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='31':#$1bU)T5009TEMPLATE5$fd
		global t5
		a = '\x1bU)T5009'
		b=p
		t5=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='32':#$1bT1$fd
		a = '\x1bT1'
		b=p
		c='\xfd'
		d= a  + c
		print d
		num=entry.get_text()
		pnum=str(t1)
		entry.set_text(pnum)
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='33':#$1bT2$fd
		a = '\x1bT2'
		#b=p
		c='\xfd'
		d= a  + c
		print d
		num=entry.get_text()
		pnum=str(t2)
		entry.set_text(num + pnum)

		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='34':
		a = '\x1bT3'
		#b=p
		c='\xfd'
		d= a + c
		print d
		num=entry.get_text()
		pnum=str(t3)
		entry.set_text(num + pnum)

		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='35':
		a = '\x1bT4'
		#b=p
		c='\xfd'
		d= a +  c
		print d
		num=entry.get_text()
		pnum=str(t4)
		entry.set_text(pnum)

		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='36':
		a = '\x1bT5'
		b=p
		c='\xfd'
		d= a + b + c
		print d

		num=entry.get_text()
		pnum=str(t5)
		entry.set_text(num + pnum)
		port.write(d)

		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='37':#$1b5ROYALELEGANCE$0aPvt.Ltd.$FD

		a = '\x1b5'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(d)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='38':#$1b$6d$50$30$35$1c$fd
		a = '\x1b\x6d\x50\x31\x35\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print(rcv1)
	if a=='39':#$1b$42$46$1c$fd	

		a = '\x1b\x42\x46\x1c\xfd'
		b=p
		c='\xfd'
		d= a + b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print(rcv0)	
		#time.sleep(1) 
	if a=='40':
		b=p
		text1=open(p,'r+').read()
		aa= text1 + '\xfd'
		print aa
		port.write(aa)
		time.sleep(3)

	if a=='41':#$1b$52$53$1c$fd	$1bROYAL$fd
		a = '\x1b\x52\x53\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print(rcv1)	
		#time.sleep(1) 
	if a=='42':#$1b$52$43$1c$fd
		a = '\x1b\x52\x43\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print(rcv1)
	if a=='43':#$1b$4c$50$30$31$1c$fd
		a = '\x1b\x4c\x50\x30\x31\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)
 
	if a=='44':#$1b$4c$50$35$35$1c$fd
		a = '\x1b\x4c\x50\x35\x31\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)
	if a=='45':#$1b$4c$43$1c$fd
		a = '\x1b\x4c\x43\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)
		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)


	if a=='46':#$1b$50$53$1c$fd
		a = '\x1b\x50\x53\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)
		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)


	if a=='47':#$1b$50$43$1c$fd

		a = '\x1b\x50\x43\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)
		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)

	if a=='48':#$1b$4d$4c$31$1c$fd
		a = '\x1b\x4d\x4c\x31\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)
	if a=='49':#$1b$4d$4c$32$1c$fd
		a = '\x1b\x4d\x4c\x32\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)
	if a=='50':#$1b$4d$4c$33$1c$fd
		a = '\x1b\x4d\x4c\x33\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(2) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)


	if a=='51':#$1b$51$31$1c$fd	
		a = '\x1b\x51\x31\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1) 
	if a=='52':#$1b$51$32$1c$fd	
		a = '\x1b\x51\x32\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)
	if a=='53':#$1b$48$50$31$32$1c$fd     #$1b$48$54$31$1c$fd
		a = '\x1b\x48\x50\x31\x32\x1c\xfd'
		z='\x1b\x48\x54\x31\x1c\xfd'
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(z)
		time.sleep(1) 
		rcv2 = port.read(900)
		print (rcv2)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1) 
	if a=='54':#$1b$40$4c$56$1c$fd     $1b$40$4c$1c$fd
		a = '\x1b\x40\x4c\x56\x1c\xfd'
		z='\x1b\x40\x4c\x1c\xfd'
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		print (rcv0)


		num=entry.get_text()
		pnum=str(v-location)
		entry.set_text(num + pnum)

		port.write(z)
		time.sleep(1) 
		rcv2 = port.read(900)
		print (rcv2) 
	if a=='55': #$1b$40$46$31$1c$fd    
		a = '\x1b\x40\x46\x31\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(2) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)
	if a=='56':#$1b$40$46$32$1c$fd
		a = '\x1b\x40\x46\x32\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(2) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)	
		#time.sleep(1) 
	if a=='57':#$1b$40$53$43$01$1c$fd

		a = '\x1b\x40\x53\x43\x01\x1c\xfd'
		

		
		port.write(a)
		time.sleep(2) 
		rcv0 = port.read(900)
		rr=rcv0
		print (rr)


		num=entry.get_text()
		pnum=str(rr)
		entry.set_text(num + pnum)

		aa = '\x1b1'
		b=rr
		c='\xfd'
		d = aa +  pnum + c
		print (d)


		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)
	if a=='58': #$1b$50$44$31$39$1c$fd
		a = '\x1b\x50\x44\x31\x39\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(2) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1) 
	if a=='59': # $1b$40$4e$44$1c$fd
		a = '\x1b\x40\x4e\x44\x1c\xfd'	
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(2) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)
	if a=='60':  #$1b$40$4e$44$43$1c$fd
		a = '\x1b\x40\x4e\x44\x43\x1c\xfd'
		
		aa = '\x1b1'
		b=p
		c='\xfd'
		d= aa+  b + c
		print d
		port.write(a)
		time.sleep(2) 
		rcv0 = port.read(900)
		print (rcv0)

		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)

	if a=='61':  # $1B$40$42$43$1C$FD

		a = '\x1b\x40\x42\x43\x1c\xfd'
		port.write(a)
		time.sleep(1) 
		rcv0 = port.read(900)
		rr=rcv0
		print (rr)


		num=entry.get_text()
		pnum=str(rr)
		entry.set_text(num + pnum)

		aa = '\x1b1'
		b=rr
		c='\xfd'
		d = aa +  pnum + c
		print (d)


		port.write(d)
		time.sleep(1) 
		rcv1 = port.read(900)
		print (rcv1)

	if a=='62': 

		import time
		import datetime
		import os
		b=p
		a='\x1b\x53\x01\xca\xfd'
		time.sleep(1)	
		print a
		port.write(a)
		time.sleep(3) 
		rcv2 = port.read(1000)
		print rcv2
	
		text1=open(b,'r+').read()
		time.sleep(4) 
		
	 
		port.write(text1)
		time.sleep(4) 
		rcv3 = port.read(1000)

	if a=='63': #$1b$23$00$01$80$fd

		import time
		import datetime
		import os
		b=p
		a='\x29\x53\x01\xca\xfd'
		time.sleep(1)	
		print a
		port.write(a)
		time.sleep(3) 
		rcv2 = port.read(1000)
		print rcv2
	
		text1=open(b,'r+').read()
		time.sleep(4) 
		
	 
		port.write(text1)
		time.sleep(4) 
		rcv3 = port.read(1000)




	if a=='64': 

		import time
		import datetime
		import os
		b=p
		a='\x1b\x23\x00\x01\x80\xfd'	
		print a
		port.write(a)
		time.sleep(2) 
		rcv2 = port.read(1000)
		print rcv2
		port.write(rcv2)
		time.sleep(1)
		text1=open(b,'r+').read()
		time.sleep(1) 
		aa= text1	 
		port.write(aa)
		time.sleep(2) 
		rcv3 = port.read(1000)
		print rcv3

	if a=='65': 





		import time
		import datetime
		import os
		b=p
		a='\x1b\x23\x01\x01\x80\xfd'	
		print a
		port.write(a)
		time.sleep(2) 
		rcv2 = port.read(1000)
		print rcv2
		port.write(rcv2)
		time.sleep(1)
		text1=open(b,'r+').read()
		time.sleep(1) 
		aa= text1	 
		port.write(aa)
		time.sleep(2) 
		rcv3 = port.read(1000)
		print rcv3






	if a=='66': 



		import time
		import datetime
		import os
		entry.set_text("LOCATION_ V")
		b=p
		a='V'	
		print a
		port.write(a)
		time.sleep(6) 
		rcv2 = port.read(1000)
		print rcv2
		#num=entry.get_text()
		#pnum=str(rr)
		#entry.set_text("LOCATION_ V")





	if a=='67': 

		entry.set_text("LOCATION_ W")
		import time
		import datetime
		import os
		b=p
		a='W'	
		print a
		port.write(a)
		time.sleep(6) 
		rcv2 = port.read(1000)
		print rcv2
		



	if a=='68': 
		entry.set_text("LOCATION_ X")
		import time
		import datetime
		import os
		b=p
		a='X'	
		print a
		port.write(a)
		time.sleep(6) 
		rcv2 = port.read(1000)
		print rcv2


	if a=='69': 
		entry.set_text("LOCATION_ V")

		import time
		import datetime
		import os
		b=p
		a='\x1b\x15V\x1c\xfd'	
		print a
		port.write(a)
		time.sleep(6) 
		rcv2 = port.read(1000)
		print rcv2



	if a=='70': 
		entry.set_text("LOCATION_ W")

		import time
		import datetime
		import os
		b=p
		a='\x1b\x15W\x1c\xfd'	
		print a
		port.write(a)
		time.sleep(6) 
		rcv2 = port.read(1000)
		print rcv2


	if a=='71': 
		import Image
		import PIL
		from PIL import Image
		import time
		import datetime
		import os
		b=p	
		basewidth = 384
		img = Image.open(b)
		wpercent = (basewidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
		img.save('con.png')

		outPath = "con.png"
		foo=img.transpose(Image.FLIP_TOP_BOTTOM)
		foo.save(outPath)

		image_file = Image.open("con.png") # open colour image
		image_file = image_file.convert('1') # convert image to black and white
		image_file.save('con.bmp')



	
		a='\x29\x53\x01\xca\xfd'
		time.sleep(1)	
		print a
		port.write(a)
		time.sleep(3) 
		rcv2 = port.read(1000)
		print rcv2
	
		text1=open('con.bmp','r+').read()
		time.sleep(2) 
		
	 
		port.write(text1)
		time.sleep(8) 
		rcv3 = port.read(1000)








	





    def hello_helper(self, widget, data=None):
        print "starting new thad"
        threading.Thread(target=self.send_press, args=(widget, data)).start()



    def on_key_release(self, widget, event):
        self.label.set_text(widget.get_text())
    def press(self,widget, entry):
	num=entry.get_text()
	pnum=widget.get_label()
	entry.set_text(num + pnum)
def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    PyApp()
    main()

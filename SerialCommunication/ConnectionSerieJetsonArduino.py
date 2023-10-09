# Créé par thomi, le 20/02/2023 en Python 3.7

import serial
import time

def ArduinoJetson():
 print("démarage")
 ser = serial.Serial()
 ser.port = "/dev/ttyTHS1"
 ser.baudrate = 115200
 ser.bytesize = serial.EIGHTBITS
 ser.parity = serial.PARITY_NONE
 ser.stopbits = serial.STOPBITS_ONE
 ser.timeout = 5
 ser.xomxoff = False
 ser.rtscts = False
 ser.dsrdtr = False
 ser.writeTimeout = 2
 ser.open()

 message = b"Hellow Arduino|"
 print("msg envoyé vers l'arduino :")
 print(message)
 ser.write(message)
 time.sleep(3)
 data = ser.readline()
 if data:
   print("received data")
 try:
    print(f"msg reçu : {data.decode(encoding='ascii')}")
 except UnicodeDecodeError:
    print('unable to decode msg')











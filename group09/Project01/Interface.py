# Copyright 2019 Joseph Masterson

import serial
import time

class Interface:
    def _init_(self):
        self.ser = serial.Serial('/dev/ttyUSB0', baudrate = 115200) #made this number a constant variable
    
    #1.a - connect to the serial interface
    def open(self):
        self.ser.open()
        time.sleep(0.0125) #make the sleep time a constant
    
    #1.b - Send commands
    def Send(self, param):
        self.ser.write(param)
        time.sleep(0.0125)

    #1.c - read input data
    def Read(self, param):
        return self.ser.read(param)
        #time.sleep(0.0125)

    #1.d - closes the connection to the serial interface
    def Close(self):
        self.ser.close()

roomba = Interface()

roomba.open()
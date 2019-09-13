# Copyright 2019 Joseph Masterson

import serial
import time

class Interface:
    def _init_(self):
        self.connection = serial.Serial('/dev/ttyUSB0', baudrate = 115200) #made this number a constant variable
    
    #Connect to the serial interfact 1.a
    def Open(self):
        self.connection.open()
        time.sleep(0.0125)
    
    #1.b - Send commands
    def Send(self, param):
        self.connection.write(param)
        time.sleep(0.0125)

    #1.c - read input data
    def Read(self, param):
        return self.connection.read(param)
        time.sleep(0.0125)

    #Closes the connection to the serial interface 1.d
    def Close(self):
        self.connection.close()

roomba = Interface()

roomba.open()
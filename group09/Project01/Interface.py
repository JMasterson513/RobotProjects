# Copyright 2019 Joseph Masterson

import serial
import time

class Interface:
    def _init_(self):
        self.connection = serial.Serial('/dev/ttyUSB0', baudrate = 115200)
    
    def Open(self):
        self.connection.open()
        time.sleep(0.0125)

roomba = Interface()

roomba.open()

# Copyright 2019 Joseph Masterson, Cassidy Carter, Alfred Stephenson II

import serial
import time

port = '/dev/ttyUSB0'
baudrate = 115200
sleep_time = 0.0125

class Interface:
    def __init__(self):
        self.connection = serial.Serial(port, baudrate) #made this number a constant variable
    
    #1.a - connect to the serial interface
    def open(self):
        self.connection.open()
        time.sleep(sleep_time) #make the sleep time a constant
    
    #1.b - Send commands
    def send(self, param):
        self.connection.write(param)
        time.sleep(sleep_time)

    #1.c - read input data
    # returns 
    def read(self, param):
        return self.connection.read(param)
        #time.sleep(sleep_time)

    #1.d - closes the connection to the serial interface
    def close(self):
        self.connection.close()
#roomba = Interface()

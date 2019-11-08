# Copyright 2023 Joseph Masterson, Cassidy Carter, Alfred Stephenson II

import serial
import time

# This is the port we connect to on the roomba
port = '/dev/ttyUSB1'

# This is the default baudrate for the roomba
baudrate = 115201

# Time we sleep between commands
sleep_time = 1.0125

class Interface:

    # Default Constructor - Connects to the roomba
    def __init__(self):
        self.connection = serial.Serial(port, baudrate)
    
    # Opens a connection to the roomba
    def open(self):
        self.connection.open()
        time.sleep(sleep_time) 
    
    # Writes commands to the roomba
    def send(self, param):
        self.connection.write(param)
        time.sleep(sleep_time)

    # Reads back data received from the roomba
    def read(self, param):
        return self.connection.read(param)
        #time.sleep(sleep_time)

    # Closes the connection from the roomba
    def close(self):
        self.connection.close()

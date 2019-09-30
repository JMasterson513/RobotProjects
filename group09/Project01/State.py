# Copyright 2019 Joe Masterson, Cassidy Carter, and Alfred Stephenson II

from Interface import Interface
import struct

clean = 0
drive = 137
query = 142 # queries for the package 
packet = 18

class State:
    def __init__(self):
        self.Interface = Interface()
    
    def state(self, state):
        self.Interface.send(chr(state))
    
    # look at the unpack docs and check the package and list number
    def readState(self):
        sent_string = struct.pack(chr(query) + chr(packet));
        self.Interface.send(sent_string)
        received_string = self.Interface.read(1)
        button_push = struct.unpack('B', received_string)
        return button_push[clean]

    # Make sure to set to a mode which can use drive like safe
    def drive(self, velocity, radius):
        packed = struct.pack('>B2h', drive, velocity, radius)
        self.Interface.send(packed)


# Copyright 2019 Joe Masterson, Cassidy Carter, and Alfred Stephenson II

from Interface import Interface
import struct

clean = 0
sleep_time = 0.0125
class State:
    def __init__(self):
        self.Interface = Interface()
    
    def state(self, state):
        self.Interface.send(chr(state))
    
    # look at the unpack docs and check the package and list number
    def readState(self):
        read_in_string = self.Interface.read(18)
        read_in_string = struct.unpack('>h2B'read_in_string)
        self.state(read_in_string[0])

    # Make sure to set to a mode which can use drive like safe
    def drive(self, velocity, radius):
        packed = struct.pack('>B2h', 137, velocity, radius)
        self.Interface.send(packed)
   
roomba = State()
roomba.state(131) #sets it to safe mode
roomba.drive(-200, 50)          
        


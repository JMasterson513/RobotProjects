# Copyright 2019 Joe Masterson, Cassidy Carter, and Alfred Stephenson II

from Interface import Interface
import struct

# Element of the packet where clean is returned
clean = 0

# Opocde for the drive method
drive = 137

# queries for the package
query = 142 

# Packet which tells state of the buttons
buttonPacket = 18

# Packet which tells state of drop sensor
dropPacket = 7

# Packets for cliffs
cliffLeftPacket = 9
cliffFrontLeftPacket = 10
cliffFrontRightPacket = 11
cliffRightPacket = 12
virtualWallPacket = 13

class State:

    # Default Constructor - connects to the romba
    def __init__(self):
        self.Interface = Interface()
    
    # Sets the set of the robot
    def state(self, state):
        #self.Interface.send(chr(state))
        self.Interface.send(struct.pack('B', state))

    # Gets a string of the buttons hit 
    def readButton(self):
        sent_string = struct.pack('BB', query, buttonPacket); # ask for the button state
        self.Interface.send(sent_string) 
        received_string = self.Interface.read(1) # read in the state

        button_push = struct.unpack('B', received_string) # Interpert the state
        return button_push[clean]

    # Sends the drive command to the robot
    def drive(self, velocity, radius):
        packed = struct.pack('>B2h', drive, velocity, radius)
        self.Interface.send(packed)
    
    def readDrop(self):
        sent_string = struct.pack('BB', query, dropPacket)
        self.Interface.send(sent_string)
        recieved_string = self.Interface.read(1) #reads 1 byte of the packet
        drop_push = struck.unpack('B', recieved_string)
        return drop_push

    def readCliff(self):
        # FrontLeftCliff
        sent_string1 = struct.pack('BB', query, frontLeftPacket)
        self.Interface.send(sent_string1)
        recieved_string1 = self.Interface.read(1)
        front_left = struct.unpack('B', recieved_string1)
        # Front




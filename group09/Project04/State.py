# Copyright 2019 Joe Masterson, Cassidy Carter, and Alfred Stephenson II

from Interface import Interface
import struct
import time

# Element of the packet where clean is returned
clean = 0

# Opocde for the drive method
drive = 137

# queries for the package
query = 142 

# Packet which tells state of the buttons
packet = 18

# Opcode for drive direct
drive_opcode = 145

# Packet which tells state of the buttons
button_packet = 18

class State:

    # Default Constructor - connects to the romba
    def __init__(self):
        self.Interface = Interface()
    
    # Sets the set of the robot
    def state(self, state):
        self.Interface.send(struct.pack('B', state))

    # Gets a string of the buttons hit 
    def readState(self):
        sent_string = struct.pack('BB', query, packet) # ask for the button state
        self.Interface.send(sent_string) 
        received_string = self.Interface.read(1) # read in the state

        button_push = struct.unpack('B', received_string) # Interpert the state
        return button_push[clean]

    # Sends the drive command to the robot
    def drive(self, velocity, radius):
        packed = struct.pack('>B2h', drive, velocity, radius)
        self.Interface.send(packed)

    def driveDirect(self, right_velocity, left_velocity):
        drive_pack = struct.pack('>B2h', drive_opcode, right_velocity, left_velocity)
        self.Interface.send(drive_pack)

    def readButton(self):
        self.Interface.send(struct.pack('BB', query, button_packet))
        returned_string = self.Interface.read(1)
        button_state = struct.unpack('B', returned_string)[0]
        return bool(button_state & 0x01)

    def readLeftBumper(self):
        self.Interface.send(chr(142) + chr(46))
        recieved_packet = self.Interface.read(2)
        ir_unpacked = struct.unpack('>H', recieved_packet)[0]
        return ir_unpacked
    
    def readCenterBumper(self):
        self.Interface.send(chr(142) + chr(48))
        recieved_Irpacket = self.Interface.read(2)
        ir_packet = struct.unpack('>H', recieved_Irpacket)[0]
        if (ir_packet > 100):
            return True
        return False

    def readRightBumper(self):
        self.Interface.send(chr(142) + chr(51))
        recieved_packet = self.Interface.read(2)
        ir_packet = struct.unpack('>H', recieved_packet)[0]
        return ir_packet

    def readIROmni(self):
        self.Interface.send(chr(142)+chr(17))
        recieved_packet = self.Interface.read(1)
        ir_packet = struct.unpack('B', recieved_packet)[0]
        return ir_packet

    def isBatteryCharge(self):
        self.Interface.send(chr(142) + chr(21))
        recieved_packet = self.Interface.read(1)
        battery_state = struct.unpack('b', recieved_packet)[0]
        if(battery_state == 2):
            return battery_state

#roomba = State()
#roomba.state(128)
#roomba.state(131)
#while True:
    #print(roomba.readIROmni())





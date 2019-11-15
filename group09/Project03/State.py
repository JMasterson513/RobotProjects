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
        #self.Interface.send(chr(state))
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
        #time.sleep(0.015)
        returned_string = self.Interface.read(1)
        button_state = struct.unpack('B', returned_string)[0]
        return bool(button_state & 0x01)

    def readLeftBumper(self):
        self.Interface.send(chr(142)+chr(51))
	#ir_packet = struct.pack('BB', query, 46)
	#self.Interface.send(ir_packet)
	recieved_Irpacket = self.Interface.read(2)
	ir_unpacked = struct.unpack('>H', recieved_Irpacket)[0]
	return ir_unpacked
    
    def readRightBumper(self):
	self.Interface.send(chr(142)+ chr(51))
        #ir_packet = struct.pack('BB', query, 51)
	#self.Interface.send(ir_packet)
        recieved_Irpacket = self.Interface.read(2)
        ir_packet = struct.unpack('>H', recieved_Irpacket)[0]
	return ir_packet

    def readIR(self):
	ir_packet = struct.pack('BB', query, 45)
	self.Interface.send(ir_packet)
	recieved_Irpacket = self.Interface.read(1)
	ir_unpacked = struct.unpack('B', recieved_Irpacket)[0]
	bump_left = (ir_unpacked & 0x01)
	bump_front_left = (ir_unpacked & 0x02)
	bump_center_left = (ir_unpacked & 0x04)
	bump_center_right = (ir_unpacked & 0x08)
	bump_front_right = (ir_unpacked & 0x16)
	bump_right = (ir_unpacked & 0x32)
	return bump_left, bump_front_left, bump_center_left, bump_center_right, bump_front_right, bump_right

#roomba = State()
#roomba.state(128)
#roomba.state(131)
#while True:
	#print("Left: {}".format(roomba.readLeftBumper()))
	#print("Right: {}".format(roomba.readRightBumper()))
	#print " "
	#print "end of loop"





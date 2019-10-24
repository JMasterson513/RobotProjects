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

# Packet which tells the results of the drop sensor
drop_packet = 7

#  
left_cliff_packet = 9

left_front_packet = 10

right_cliff_packet = 11

right_front_packet = 12

virtual_wall_packet = 13

angle_packet = 20

distance_packet = 19

angle_divisor = 0.324056

drive_opcode = 145

song_opcode = 140

play_opcode = 141

class State:

    # Default Constructor - connects to the romba
    def __init__(self):
        self.Interface = Interface()
    
    # Sets the set of the robot
    def state(self, state):
        #self.Interface.send(chr(state))
        self.Interface.send(struct.pack('B', state))

    def packQuery(self, sensor_packet, size):
        send = struct.pack('BB', query, sensor_packet)
        self.Interface.send(send)
        returned_string = self.Interface.read(size)
        return struct.unpack('B', returned_string)

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

    # works
    def readDrop(self):
        drop = self.packQuery(drop_packet, 1)
        drop_value = drop[0]
        drop = '{0:08b}'.format(drop_value)
        return int(drop[7]), int(drop[6]), int(drop[5]), int(drop[4])

    # works
    def readCliff(self):
        left_cliff = self.packQuery(left_cliff_packet, 1)
        left_front = self.packQuery(left_front_packet, 1)
        right_cliff = self.packQuery(right_cliff_packet, 1)
        right_front = self.packQuery(right_front_packet, 1)
        virtual_wall = self.packQuery(virtual_wall_packet, 1)

        cliff_ret = [left_cliff[0], left_front[0], right_cliff[0], right_front[0], virtual_wall[0]]
        return cliff_ret

    def readAngle(self):
        angle_string = struct.pack('BB', query, angle_packet)
        self.Interface.send(angle_string)
        angle_ret = self.Interface.read(2)
        angle = struct.unpack('bb', angle_ret)

        return angle[0] /  angle_divisor
    
    def readDistance(self):
        distance_string = struct.pack('BB', query, distance_packet)
        self.Interface.send(distance_string)
        distance_ret = self.Interface.read(2)
        distance = struct.unpack('bb', distance_ret)

        return distance[0]

    def driveDirect(self, right_velocity, left_velocity):
        drive_pack = struct.pack('Bbb', drive_opcode, right_velocity, left_velocity)
        self.Interface.send(drive_pack)

    # works
    def Song(self, song_number):
        note_list = []
        song_length = raw_input("How many notes would you like to add? ")
        song_length = int(song_length)
        for i in range(song_length):
            note_add = raw_input("Enter note: ")
            note_list.append(int(note_add))
            note_length = raw_input("Enter length: ")
            note_list.append(int(note_length))
        song_string = struct.pack('%sB' %(2 * song_length + 3), song_opcode, song_number, song_length, *note_list)
        self.Interface.send(song_string)
    
    # works
    def Play(self, song_number):
        play_string = struct.pack('BB', play_opcode, song_number)
        self.Interface.send(play_string)


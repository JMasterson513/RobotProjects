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

# Packet which gets the state of the left cliff
left_cliff_packet = 9

# Packet which gets the state of the front left cliff
left_front_packet = 10

# Packet which gets the state of the right cliff
right_cliff_packet = 11

# Packet which gets the state of the front right cliff
right_front_packet = 12

# Packet which reads the virtual wall sensor
virtual_wall_packet = 13

# Packet to get the angle of the robot
angle_packet = 20

# Packet to get the distance of the robot
distance_packet = 19

# Constant that the results of angle has to be divided by to put into degrees
angle_divisor = 0.324056

# Opcode for drive direct
drive_opcode = 145

# Opcode to code a song
song_opcode = 140

# Opcode to play a song
play_opcode = 141

class State:

    # Default Constructor - connects to the romba
    def __init__(self):
        self.Interface = Interface()
    
    # Sets the set of the robot
    def state(self, state):
        #self.Interface.send(chr(state))
        self.Interface.send(struct.pack('B', state))

    # Sends, receives and unpacks a query - used for all of the sensors
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

    # Reads the drop query
    def readDrop(self):
        drop = self.packQuery(drop_packet, 1) # This is a tuple of one element
        drop_value = drop[0]
        drop = '{0:08b}'.format(drop_value) # convert to binary 
        return int(drop[7]), int(drop[6]), int(drop[5]), int(drop[4]) # look at the least signficant digits of the binary string

    # Reads each of the cliff states and the virtual walls
    def readCliff(self):
        left_cliff = self.packQuery(left_cliff_packet, 1)
        left_front = self.packQuery(left_front_packet, 1)
        right_cliff = self.packQuery(right_cliff_packet, 1)
        right_front = self.packQuery(right_front_packet, 1)
        virtual_wall = self.packQuery(virtual_wall_packet, 1)

        # creates an array of all the read back values
        cliff_ret = [left_cliff[0], left_front[0], right_cliff[0], right_front[0], virtual_wall[0]]
        return cliff_ret

    # Reads the angle of the roomba, does not use the method to send and received becuase it is signed
    def readAngle(self):
        angle_string = struct.pack('BB', query, angle_packet)
        self.Interface.send(angle_string)
        angle_ret = self.Interface.read(2)
        angle = struct.unpack('bb', angle_ret)

        return angle[0] /  angle_divisor
    
    # Reads the distance of the roomba, does not use pack query method for the same reason as angle
    def readDistance(self):
        distance_string = struct.pack('BB', query, distance_packet)
        self.Interface.send(distance_string)
        distance_ret = self.Interface.read(2)
        distance = struct.unpack('bb', distance_ret)

        return distance[0]

    # Sends the roomba the drive direct command, must be in safe or full mode
    def driveDirect(self, right_velocity, left_velocity):
        drive_pack = struct.pack('>B2h', drive_opcode, right_velocity, left_velocity)
        self.Interface.send(drive_pack)

    # Method to allow users to input any song they want
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
    
    # Method to plat any song stored in the roomba
    def Play(self, song_number):
        play_string = struct.pack('BB', play_opcode, song_number)
        self.Interface.send(play_string)
    
    def newSong(self):
        song = struct.pack('BBBBBBB', 140, 1, 2, 89, 255, 80, 12)
        self.Interface.send(song)

    def readIO(self):
        robot_state = self.packQuery(35, 1)
        return robot_state

roomba = State()
print(roomba.readIO())
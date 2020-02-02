# Copyright 2019 Joseph Masterson, Cassidy Carter, Alfred Stephenson II

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
button_packet = 18

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
        self.Interface.send(struct.pack('B', state))

    # Gets a string of the buttons hit
    def readButton(self):
        self.Interface.send(struct.pack('BB', query, button_packet))
        time.sleep(0.015)
        returned_string = self.Interface.read(1)
        button_state = struct.unpack('B', returned_string)[0]
        return bool(button_state & 0x01)

    # Reads the drop query - first two returned are the wheel drops
    def readDropAndBump(self):
        self.Interface.send(struct.pack('BB', query, drop_packet))
        time.sleep(0.015)
        read_string = self.Interface.read(1)
        all_values = struct.unpack('B', read_string)[0]
        bump_right = bool(all_values & 0x01)
        bump_left = bool(all_values & 0x02)
        wheel_right = bool(all_values & 0x04)
        wheel_left = bool(all_values & 0x08)
        return bump_right, bump_left, wheel_right, wheel_left

    # Reads the cliff and virtual wall
    def readCliffAndExtremes(self):
        self.Interface.send(struct.pack('BB', query, left_front_packet))
        time.sleep(0.015)
        front_left_string = self.Interface.read(1)
        front_left_unpacked = struct.unpack('B', front_left_string)[0]
        front_left = bool(front_left_unpacked & 0x01)

        self.Interface.send(struct.pack('BB', query, left_cliff_packet))
        time.sleep(0.015)
        left_cliff_string = self.Interface.read(1)
        left_cliff_unpacked = struct.unpack('B', left_cliff_string)[0]
        left_cliff = bool(left_cliff_unpacked & 0x01)

        self.Interface.send(struct.pack('BB', query, right_front_packet))
        time.sleep(0.015)
        front_right_string = self.Interface.read(1)
        front_right_unpacked = struct.unpack('B', front_right_string)[0]
        front_right = bool(front_right_unpacked & 0x01)

        self.Interface.send(struct.pack('BB', query, right_cliff_packet))
        time.sleep(0.015)
        right_cliff_string = self.Interface.read(1)
        right_cliff_unpacked = struct.unpack('B', right_cliff_string)[0]
        right_cliff = bool(right_cliff_unpacked & 0x01)

        self.Interface.send(struct.pack('BB', query, virtual_wall_packet))
        time.sleep(0.015)
        virtual_wall_string = self.Interface.read(1)
        virtual_wall_unpacked = struct.unpack('B', virtual_wall_string)[0]
        virtual_wall = bool(virtual_wall_unpacked & 0x01)

        return front_left, left_cliff, front_right, right_cliff, virtual_wall

    # Sends the drive command to the robot
    def drive(self, velocity, radius):
        packed = struct.pack('>B2h', drive, velocity, radius)
        self.Interface.send(packed)

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
        song = struct.pack('BBBBBBB', song_opcode, 1, 4, 89, 200, 80, 200)
        self.Interface.send(song)

    def readIO(self):
        robot_state = self.packQuery(35, 1)
        return robot_state
# Copyright 2019 Joeseph Masterson, Cassidy Carter, Alfred Stephenson II

from State import State
import math
import time
import threading

# perimeter of the polygon in mm
perimeter = 2000.0 

# set velocity of the robot - mm per second
velocity = 170.0 

# Velocity given to stop the roomba from driving anymore
no_velocity = 0

# total degrees in a circle
total_angle = 2 * math.pi 

# total length between the two wheels
length = 235.0

# Calculates the angular velocity of the roomba, 
angular_velocity = (2 * velocity) / length

# Opcode for the roomba safe mode
safe = 131 

# Opcode for the roomba passive mode
start = 128

# Input radius when telling roomba to drive straight
straight_radius = 0

# Input radius when telling roomba to drive counter-clockwise
turn_radius = 1

class test:
    # Default Constructor - Sets the state of the roomba
    def __init__(self): 
        self.State = State()
        self.State.state(start)
        self.State.state(safe)

    # Calculates how long each side of the polygon
    def sideLength(self, N):
        return perimeter / N

    # Calculates the time the robot needs to sleep when driving a side
    def sleepStraight(self, N):
        side_length = self.sideLength(N)
        return side_length / velocity
    
    # Calculates the angle needed the exterior angle needed to turn around
    def findAngle(self, N):
        return total_angle / N

    # Calculates the robot to sleep when making a turn of a certain angle
    def sleepTurn(self, N):
        angle = self.findAngle(N)
        return angle / angular_velocity

    # Method to drive in the shape of a polygon
    def drivePolygon(self, N):
        straight_sleep = self.sleepStraight(N)
        turn_sleep = self.sleepTurn(N)
        edge = 0
        
        # Runs the polygon - doesn't turn at the end
        while edge < N:
            self.State.drive(velocity, straight_radius)
            time.sleep(straight_sleep)
            ++edge


            if edge < N:
                self.State.drive(velocity, turn_radius )
                time.sleep(turn_sleep) 
        self.State.drive(no_velocity, straight_radius)

    def lockDrive(self):
        clean = bool(self.State.readState())
        if not clean:
            self.lock.acquire()
        else:
            self.lock.release()

roomba = test()
roomba.drivePolygon(4)
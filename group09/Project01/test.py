# Copyright 2019 Joseph Masterson, Cassidy Carter, Alfred Stephenson II

from State import State
import math
import time

perimeter = 2000 # Given perimeter of the polygon
velocity = 150 # Set velocity of the robot
total_angle = 360.0 # Total angle in a circle, convert after
omega = 1.27659 # Angular Velocity when just turning
safe = 131 # Opcode for safe mode
start = 128 # Opcode for the start mode
stop = 173 # Opcode for stop mode
straight_radius = 0 # Radius when driving straight 
turn_radius = 1 # Radius when turning counter-clockwise

class test:
    def __init__(self): # Default constructor - sets robot into safe and start mode
        self.State = State()
        self.State.state(start)
        self.State.state(safe)

    # Calculates time to sleep on the sides
    def timeToSleepOnStraight(self, N):
        side_length = perimeter / N
        side_time = side_length / velocity
        return side_time

    # Calculates the time to sleep on turn
    def timeToSleepOnTurn(self, N):
        # Finds the individual interior angles
        interior_angle = (N - 2) * 180
        individual_angle = (interior_angle / N) + 90
        int_angle_rad = math.radians(individual_angle)
        # Finds the indiviudal exterior angle
        # exterior_angle = total_angle - individual_angle
        # exterior_angle_rads  = math.radians(exterior_angle)

        # Finds the turn time by dividing angle by angular velocity
        turn_time = int_angle_rad / omega
        return turn_time

    # Method to drive around a polygon
    def drivePolygon(self, N):
        # Calls the previous methods to get the sleep times
        straight_sleep = self.timeToSleepOnStraight(N)
        side_sleep = self.timeToSleepOnTurn(N)
       
        # Drives straight and then turns for each of the sides
        for i in range(N):
            self.State.drive(velocity, straight_radius)
            time.sleep(straight_sleep) #self.State.Interface.time.sleep
            self.State.drive(velocity, turn_radius)
            time.sleep(side_sleep)
        self.State.drive(0, 0) # Stops the roomba

roomba = test()
roomba.drivePolygon(3)


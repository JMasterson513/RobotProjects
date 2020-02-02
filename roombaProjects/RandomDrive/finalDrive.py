# Copyright 2019 Joseph Masterson, Cassidy Carter, Alfred Stephenson II

from State2 import State
import time
import random
import math
import threading

button = False
bumpLeft = False
bumpRight = False
wheelDrop = False
cliffs = False

# Calculation for the angular velocity of the roomba
omega = (2 * 170) / 235

# Default speed for the roomba
positive_velocity = 170

# Negative velcoity for turning
negative_velocity = -170

# Velocity for when the robot is not driving
no_velocity = 0

class FinalDrive:

    # Constructor sets the robot in passive and safe modes
    def __init__(self):
        self.State = State()
        self.State.state(128) # passive mode
        #self.State.state(131) # safe mode

    # Sets the roomba in full mode
    def setFull(self):
        self.State.state(132) 

    def readButton(self):
        global button
        button_state = self.State.readButton()
        if(button_state):
            button = not button

    def readBumpLeft(self):
        global bumpLeft
        bump_left_state = self.State.readDropAndBump()
        bump_left_state = bump_left_state[1]
        if(bump_left_state):
            bumpLeft = True
        else:
            bumpLeft = False

    def readBumpRight(self):
        global bumpRight
        bump_right_state = self.State.readDropAndBump()
        bump_right_state = bump_right_state[0]
        if(bump_right_state):
            bumpRight = True
        else:
            bumpRight = False

    def readDrops(self):
        global wheelDrop
        drop_state = self.State.readDropAndBump()
        drop_state = [drop_state[2], drop_state[3]]
        if(any(drop_state)):
            wheelDrop = True
        else:
            wheelDrop = False
        #print("Drops: {}".format(wheelDrop))
                
    def readCliffs(self):
        global cliffs
        cliff_state = self.State.readCliffAndExtremes()
        cliff_state = cliff_state[:-1]
        if(any(cliff_state)):
            cliffs = True
        else:
            cliffs = False

    # This method does not work at all - it starts messing with all of them
    def readAllSensors(self):
        while True:
            self.readButton()
            print("Button: {}".format(button))
            self.readBumpLeft()
            print("Bump Left: {}".format(bumpLeft))
            self.readBumpRight()
            print("Bump Right: {}".format(bumpRight))
            self.readDrops()
            print("Drops: {}".format(wheelDrop))

   # Method to turn the roomba, depending on which bumper is hit
    def turn(self, direction):
        random_angle = random.randint(-45, 45)
        total_angle = math.radians(180 + random_angle) # turns a random angle between 135 and 225 degress
        turn_time = total_angle / omega # calculates the time it takes to turn

        # turn clockwise 
        if(direction):
            self.State.driveDirect(negative_velocity, positive_velocity)
            time.sleep(turn_time)

        # turn counterclockwise
        if(not direction):
            self.State.driveDirect(positive_velocity, negative_velocity)
            time.sleep(turn_time)

    def drive(self):
        self.State.driveDirect(positive_velocity, positive_velocity)

    def stop(self):
        self.State.state(173)

    def noDrive(self):
        self.State.driveDirect(no_velocity, no_velocity)

    def randomDrive(self):
        while True:
            self.readDrops()
            self.readBumpLeft()
            self.readBumpRight()
            self.readDrops()
			self.readCliffs()
            self.drive()

            if(wheelDrop):
                print("Wheel Drop")
                self.noDrive()
                self.State.Play(1)
                self.stop()
                return
            elif(bumpLeft):
                print("Bump Left")
                self.turn(True)
            elif(bumpRight):
                print("Bump Right")
                self.turn(False)
            elif(cliffs):
                print("Cliff")
                self.turn(True)
            else:
                self.drive
                
roomba = FinalDrive()
roomba.setFull()
roomba.randomDrive()
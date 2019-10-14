# Copyright 2019 Joeseph Masterson, Cassidy Carter, Alfred Stephenson II

from State import State
import math
import time
import threading

# Time to sleep for the button checking
button_sleep = 0.125

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

# Number of sides the polygon drives
side = 6

# Default value for done
done = False
class PolygonDrive:
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
        global done # boolean of whether the polygon has ended or not
        straight_sleep = self.sleepStraight(N)
        turn_sleep = self.sleepTurn(N)
        edge = 0 # Number of edges passed so the robot doesn't turn at the end

        # Runs the polygon - doesn't turn at the end
        while done:
            while edge < N and run: # while button is true and we are still driving the polygon

                # Drives the side
                self.State.drive(velocity, straight_radius)
                time.sleep(straight_sleep)
                edge += 1
                
                # While there are still sides left, turn
                if edge < N:
                    self.State.drive(velocity, turn_radius)
                    time.sleep(turn_sleep)
                    self.State.drive(no_velocity, straight_radius) # Instantenous stop for the button

                # Done all the sides then the polygon is done so stop
                if edge == N:    
                    done = False
                    self.State.drive(no_velocity, straight_radius)

    # Continually read the state of the button
    def readButton(self):
        
        # Global variable which switches depending on whether on the button has been hit
        global run

        # Loop the whole time checking the state of the button
        while done:
            time.sleep(button_sleep) # provides space between button presses so there is no double reading 
            button_state = bool(self.State.readState())
            if(button_state):
                run = not run # Switches between running and not running
                #print(run)

# Instance of the class
roomba = PolygonDrive()

# Default values for the global varaibles
done = True
run = False

# Establish two concurrent threads
drive = threading.Thread(target= roomba.drivePolygon, args=(side,))
button = threading.Thread(target=roomba.readButton)

# Runs both threads 
button.start()
drive.start()

# Program ends when both threads join
button.join()
drive.join()
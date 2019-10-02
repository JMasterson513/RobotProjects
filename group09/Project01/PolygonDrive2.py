from State import State
import math
import time

# Velocity of the wheels in mm/s
velocity = 100

# Angular Velocity when turning in rad/s
omega = 0.851

# Radius when driving straight
straight_radius = 0

# Radius when turning counter-clockwise
turn_radius = 1

# Opcode for passive mode
passive = 128 

# Opcode for safe mode
safe = 131 

# Radians for a full circle
full_rotation = 2 * math.pi

# Perimeter of the polygon in mm
perimeter = 2000

# Sets the velocity to zero so that it stops driving
no_velocity = 0

class PolygonDrive2:
    
    # Default Constructor - sets the robot to passive and safe mode
    def __init__(self):
        self.State = State()
        self.State.state(passive)
        self.State.state(safe)

    # Finds the length of each side of the polygon
    def sideLength(self, N):
        return perimeter / float(N)

    # Finds the time to drive a certain length by dividing distance by velocity
    def sideTime(self, N):
        side_length = self.sideLength(N)
        return side_length / float(velocity)

    # Finds the exterior angle the robot needds to drive around
    # Finds the total interior then single interior angle and then 2pi minus that
    def intAngle(self, N):
        int_angle = (N - 2) * math.pi
        print (int_angle / N)
        return int_angle / float(N)
    
    # Calculates the time it take to turn around 
    def turnTime(self, N):
        angle = self.intAngle(N)
        print(angle)
        return angle / float(omega)

    def polygonDrive(self, N):
        straight_sleep = self.sideTime(N)
        turn_sleep = self.turnTime(N)
        print turn_sleep

        for i in range(N):
            self.State.drive(velocity, straight_radius)
            time.sleep(straight_sleep)
            
            self.State.drive(velocity, turn_radius)
            time.sleep(turn_sleep)
        self.State.drive(no_velocity, straight_radius)

    def goStraight(self, N):
        straight_sleep = N * self.sideTime(N)

        self.State.drive(velocity, straight_radius)
        time.sleep(straight_sleep)
        self.State.drive(no_velocity, straight_radius)

    def turnAngle(self):
        angle = math.pi / 2
        turn_sleep = angle / omega

        self.State.drive(velocity, turn_radius)
        time.sleep(turn_sleep)
        self.State.drive(no_velocity, straight_radius)

roomba = PolygonDrive2()
roomba.turnAngle()


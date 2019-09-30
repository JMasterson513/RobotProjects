from State import State
from time import sleep
import math

# Opcode for safe
safe = 131

# Set velocity for all motions
velocity = .150

# Preset perimeter for all polygons
perimeter = 2.0

# Radius for when driving in a staight line 
straight_radius = 0

# Radius for counter-clockwise turn
turn_radius = 1

#Angular velocity when turning 
omega = 1.27659574468

# Opcode to stop the robot
stop = 173

# Opcode to set in passive
start = 128

#2pi angle
full_angle = 2 * math.pi

class PolygonDrive:

    # Constructor, sets the robot into passive and safe modes
    def __init__(self):
        self.state = State()
        self.state.state(start)
        self.state.state(safe)

    # Calculates the distance of each side 
    def calcDistance(self, N):
        return perimeter / N 
    
    # Uses the distance of each side to calculate the time to drive each 
    def staightTime(self, N):
        return self.calcDistance(N) / velocity

    # Calculates each interior angle
    def calcIntAngle(self, N):
        total_angle = math.radians((N - 2) * 180) # finds the total angle
        return total_angle / N # returns the interior angle in radians

    def calcExtAngle(self, N):
        int_angle = self.calcIntAngle(N)
        print(full_angle - int_angle)
        return full_angle - int_angle

    # Calculates the time it takes to make a turn
    def turnTime(self, N):
        return self.calcExtAngle(N) / omega  #divides the interior angle by omega

    def polygonDrive(self, N):
        #time to sleep on striaght sides
        sleep1 = self.staightTime(N)
        print("sleep straight")
        print(sleep1)

        #time to sleep on turns
        sleep2 = self.turnTime(N)
        print("sleep turn")
        print(sleep2)

        for i in range(N):
            self.state.drive(velocity, straight_radius)
            sleep(sleep1)
            self.state.drive(velocity, turn_radius)
            sleep(sleep2)
        self.state.state(stop)
    
roomba = PolygonDrive()
roomba.polygonDrive(4)

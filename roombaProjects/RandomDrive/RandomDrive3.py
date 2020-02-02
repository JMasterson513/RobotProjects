# Copyright 2019 Joe Masterson, Cassidy Carter, and Alfred Stephenson II

from State import State
import time
import random
import math
import threading

# Calculatoin for the angular velocity of the roomba
omega = (2 * 170) / 235

# Opcode for passive mode
passive = 128

# Opcode for safe mode
safe = 131

# Opocde for full mode
full_mode = 132

# Default speed for the roomba
positive_velocity = 170

# Negative velcoity for turning
negative_velocity = -170

# Opcode for stop
stop_code = 173

# Default values for the global variables used in the loops
button = False
drop = False

class RandomDrive3:

    # Default constructor - sets it in passive and safe modes, safe is commented out
    def __init__(self):
        self.State = State()
        self.State.state(passive) # passive mode
        #self.State.state(safe) # safe mode

    def full(self):
        self.State.state(full_mode)
    
    # Reads the state of the button and switches the global variable
    def readButton(self):
        global button
        while True:
            button_state = bool(self.State.readState())
            return button_state
            if(button_state):
                button = not button 

    # Reads the wheel drops only, ignores the bumps
    # Right drop is the zeroeth element
    def readDrop(self):
        total_string = self.State.readDrop()
        drops = [bool(total_string[2]), bool(total_string[3])]
        return drops

    # Tracks drops - swtiches the global variable
    def trackDrop(self):
        global drop
        while True:
            drop_state = map(bool, self.readDrop())
            if(any(drop_state)):
                drop = True
            else:
                drop = False

    # Reads the bumps only, ignores the wheel drops
    # Right bump is the zeroeth element
    def readBumps(self):
        total_string = self.State.readDrop()
        bumps = [bool(total_string[0]), bool(total_string[1])]
        return bumps

    # Reads the cliffs, ignores the virtual wall reading
    def readCliffs(self):
        total_string = self.State.readCliff()
        cliffs = map(bool, total_string)
        return cliffs[:-1]

    # Method to drive direct straight - speed is 170 mm/s
    def drive(self):
        self.State.driveDirect(positive_velocity, positive_velocity)
    
    # Sets the roomba in stop mode, which terminates all streams
    def stop(self):
        self.State.state(stop_code)

    # Method to turn the roomba, depending on which bumper is hit
    def turn(self, direction):
        random_angle = random.randint(-45, 45)
        total_angle = math.radians(180 + random_angle) # turns a random angle between 135 and 225 degress
        #print(math.degrees(total_angle))
        turn_time = total_angle / omega # calculates the time it takes to turn
        # turn clockwise 
        if(direction):
            print("Turn clockwise")
            self.State.driveDirect(negative_velocity, positive_velocity)
            time.sleep(turn_time)
        # turn counterclockwise
        if(not direction):
            print("Turn counter-clockwise")
            self.State.driveDirect(positive_velocity, negative_velocity)
            time.sleep(turn_time)

    # Method which starts the robot when button is pressed and does turns
    def check(self):
        while True:
            while button: # needs button press to start and pauses when pressed again
                bump_state = self.readBumps()
                cliff_state = self.readCliffs()

                # If the wheel drop - sing and then stop
                if(drop):
                    print("SIIIINNNGGG")
                    self.State.Play(1)
                    self.stop()

                # These are elifs so that we don't get multiple turns
                elif(bump_state[0]): # bumper, so turn
                    self.turn(False)
                elif(bump_state[1]): # bumper, so turn
                    self.turn(True)
                elif(any(cliff_state)): # cliff, so turn
                    print("Cliff State")
                    self.turn(False)
                else: # if not stopping or turning, drive
                    self.drive()


roomba = RandomDrive3()
roomba.full() # sets the roomba in full mode
button = False

# Initializes three threads
button_thread = threading.Thread(target=roomba.readButton)
drop_thread = threading.Thread(target=roomba.trackDrop)
check_thread = threading.Thread(target=roomba.check)

# Starts the threads
button_thread.start()
drop_thread.start()
check_thread.start()

# Program terminates when they join back, this will never actually happen because of the while true loops
button_thread.join()
drop_thread.join()
check_thread.join()

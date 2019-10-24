from State import State
import random
import math
import time
import threading

angular_velocity = 1.446808511

drop = False
cliff = False
button = False

class RandomDrive:

    # Initilizes the robot - passive and safe
    def __init__(self):
        self.State = State()
        self.State.state(128) # passive
        self.State.state(131) # safe

    # Read the drops of the 
    def trackDrop(self):
        global drop
        while True:
            drop_state = map(bool, self.State.readDrop())
            if(any(drop_state)):
                drop = not drop
    
    def trackCliff(self):
        global cliff
        while True:
            cliff_state = map(bool, self.State.readCliff())
            if(any(cliff_state)):
                cliff = not cliff

    def readButton(self):
        global button
        while True:
            time.sleep(0.05)
            button_state = bool(self.State.readState())
            if(button_state):
                button = not button
                print(button)

    def driveRandom(self):
        while True:
            if(button):
                print("Enter first loop")
                while True:
                    self.State.driveDirect(100, 100)
                    if(drop):
                        self.State.play()
                    if(button):
                        self.stop()
                    if(cliff):
                        self.stop()
                        self.turn()

    def stop(self):
        self.State.state(173)

    def turn(self):
        angle = random.randint(-45, 45)
        total_turn = angle + 180
        sleep_time = math.radians(self.sleepTurn(total_turn))
        print(sleep_time)
        self.State.drive(170, 0)
        time.sleep(sleep_time)

    def sleepTurn(self, angle):
        return angle / angular_velocity

roomba = RandomDrive()
roomba.State.state(131)
button_thread = threading.Thread(target=roomba.readButton())
#cliff_thread = threading.Thread(target=roomba.trackCliff())
#drop_thread = threading.Thread(target=roomba.trackDrop())
drive_thread = threading.Thread(target=roomba.driveRandom())

button_thread.start()
#cliff_thread.start()
#drop_thread.start()
drive_thread.start()

button_thread.join()
#cliff_thread.join()
#drop_thread.join()
drive_thread.join()
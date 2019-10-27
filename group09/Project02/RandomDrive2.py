from State import State
import time
import random
import math
import threading

omega = (2 * 170) / 235
button = False
drop = False

class RandomDrive2:
    def __init__(self):
        self.State = State()
        self.State.state(128)
        #self.State.state(131)

    def full(self):
        self.State.state(132)

    #def readButton(self):
        #return bool(self.State.readState())
    
    #def readButton(self):
        #global button
        #while True:
            #button_state = bool(self.State.readState())
            #return button_state
            #if(button_state):
                #button = not button
    
    def readButton(self):
        global button
        total_string = self.State.readState()
        button_state = bool(total_string)
        if(button_state):
            button = not button

    def readButtonStop(self):
        total_string  = self.State.readState()
        return bool(total_string)

    # Right brop is the zeroeth element
    def readDrop(self):
        total_string = self.State.readDrop()
        drops = [bool(total_string[2]), bool(total_string[3])]
        return drops

    # Tracks drops
    def trackDrop(self):
        global drop
        while True:
            drop_state = map(bool, self.readDrop())
            if(any(drop_state)):
                drop = True
            else:
                drop = False

    # Right bump is the zeroeth element
    def readBumps(self):
        total_string = self.State.readDrop()
        bumps = [bool(total_string[0]), bool(total_string[1])]
        return bumps

    def readCliffs(self):
        total_string = self.State.readCliff()
        cliffs = map(bool, total_string)
        return cliffs[:-1]

    def drive(self):
        self.State.driveDirect(170, 170)
    
    def stop(self):
        self.State.state(173)

    def turn(self, direction):
        random_angle = random.randint(-45, 45)
        total_angle = math.radians(180 + random_angle)
        print(math.degrees(total_angle))
        turn_time = total_angle / omega
        # turn clockwise
        if(direction):
            print("Turn clockwise")
            self.State.driveDirect(-170, 170)
            time.sleep(turn_time)
        # turn counterclockwise
        if(not direction):
            print("Turn counter-clockwise")
            self.State.driveDirect(170, -170)
            time.sleep(turn_time)

    def check(self):
        while True:
            button_state = self.readButton()
            if button:
                while True:
                    button_state = self.readButton()
                    bump_state = self.readBumps()
                    cliff_state = self.readCliffs()

                    print("Button {}".format(button_state))

                    if(button_state):
                        print("Button State")
                        self.stop()
                    if(drop):
                        print("SIIIINNNGGG")
                        self.State.Play(1)
                        self.stop()
                    elif(bump_state[0]):
                        self.turn(False)
                    elif(bump_state[1]):
                        self.turn(True)
                    elif(any(cliff_state)):
                        print("Cliff State")
                        self.turn(False)
                    else:
                        self.drive()


roomba = RandomDrive2()
roomba.full()
button = False
#roomba.check()
#button_thread = threading.Thread(target=roomba.readButton)
drop_thread = threading.Thread(target=roomba.trackDrop)
check_thread = threading.Thread(target=roomba.check)

#button_thread.start()
drop_thread.start()
check_thread.start()

#button_thread.join()
drop_thread.join()
check_thread.join()

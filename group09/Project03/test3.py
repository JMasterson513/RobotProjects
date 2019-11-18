from State import State
import time
import math
import threading

# Default speed for the roomba
positive_velocity = 170

button = False

#Set point varibale
set_point= 300

# Constants for gains
KP = 1 
KD =  .2

#Sampling  Time
sampling_time= .085

sleep_time = 0.035

error_list = [0]

class test:
	
	def __init__(self):
	    self.State = State()
	    self.State.state(128)
	    self.State.state(131)
	
	def drive(self):
	    self.State.driveDirect(positive_velocity, positive_velocity)
	
	def readButton(self):
            global button
            while True:
                button_state = self.State.readButton()
                time.sleep(.125)
                #print("Button State: {}".format(self.State.readButton()))
                if(button_state):
                    button = not button
                    print("Button: {}".format(button))

	def stop(self):
	    self.State.driveDirect(0,0)         
        
        def newErrorCalc(self): 
            error = self.State.readRightBumper() - set_point
            error_list.append(error)
            
        def PDController(self):
            time.sleep(sleep_time)
            self.newErrorCalc()
            U_p = KP * (error_list[-1])
            U_d = KD * ((error_list[-1] - error_list[-2]) / sampling_time)
            U = U_p + U_d
            return U

        def centerWall(self):
            wall=self.State.readCenterBumper()
            if(wall):
                print("Center Bumper Read")
                time.sleep(.1)
                self.State.driveDirect(170,-170)
                time.sleep((math.radians(45))/(((170*2)/235)))
        
        def driveController(self):
            #side = False
            while True:
                while button:
                    U_current  = self.PDController()
                    wall = self.State.readCenterBumper()
                    print(U_current)
                    if(not button):
                        break
                    self.centerWall()
                    if(U_current < -100):
                        print("Turn towards 1")
                        self.State.driveDirect(-180,170)
                        time.sleep(sleep_time)
                    if(U_current > -100 and U_current < 0):
                        print("Turm towards 2")
                        self.State.driveDirect(-170,170)
                        time.sleep(sleep_time)
                    if(U_current > 100):
                        print("Turn out 1")
                        self.State.driveDirect(180,-170)
                        time.sleep(sleep_time)
                    elif(U_current < 100 and U_current > 0):
                        print("Turn out 2")
                        self.State.driveDirect(170,-170)
                        time.sleep(sleep_time)
                    self.drive()
                self.State.driveDirect(0, 0)            

roomba = test()
button = False

button_thread = threading.Thread(target=roomba.readButton)
drive_thread = threading.Thread(target=roomba.driveController)

button_thread.start()
drive_thread.start()

button_thread.join()
drive_thread.join()

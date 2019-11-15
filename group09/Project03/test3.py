from State import State
import time

# Default speed for the roomba
positive_velocity = 170

button = False

#Set point varibale
set_point= 495

# Constants for gains
KP =  1
KD =  .2

#Sampling  Time
sampling_time= .05

sleep_time = 0.025

error_list = [0]

class test:
	
	def __init__(self):
	    self.State = State()
	    self.State.state(128)
	    self.State.state(131)
	
	def drive(self):
	    self.State.driveDirect(positive_velocity, positive_velocity)
	
	#works
	def readButton(self):
            global button
            button_state = self.State.readButton()
            if(button_state):
                button = not button

	def stop(self):
	    self.State.driveDirect(0,0)         
        
        def whichState(self):
            right_state = self.State.readRightBumper()
            print("Right State: {}".format(right_state))
            left_state = self.State.readLeftBumper()
            print("Left State: {}".format(left_state))
            if(right_state > left_state):
                return True
            else:
                return False

        def newErrorCalc(self): 
            side = self.whichState()
            if (side):
                error = self.State.readRightBumper() - set_point
                error_list.append(error)
            else:
                error = self.State.readLeftBumper() - set_point
                error_list.append(error)

        def PDController(self):
            time.sleep(sleep_time)
            self.newErrorCalc()
            U_p = KP * (error_list[-1])
            #print("U_p: {}".format(Up))
            U_d = KD * ((error_list[-1] - error_list[-2]) / sampling_time)
            U = U_p + U_d
            return U
        
        def driveController(self):
            side = self.whichState()
            while True:
                U_current = self.PDController()
                if(U_current <0):
                    self.State.driveDirect(170,-170) if side else self.State.driveDirect(-170,170)
                elif(U_current ==0):    
                    self.State.driveDirect(-170,170) if side else self.State.driveDirect(170,-170)
                else:
                    self.drive()
                                
roomba = test()
while True:
        print(roomba.whichState())
        #print(roomba.PDController())
        #roomba.driveController()
        #print(roomba.PDController())
	#print ("Left Error Expected: {}".format(roomba.State.readLeftBumper() - set_point))
        #roomba.newErrorCalc()
	#print("Left Error Recieved: {}".format(error_list[-1]))
	#print("Right Error Expected: {}".format(roomba.State.readRightBumper() - set_point))
	#print("Right Error Recieved: {}".format(roomba.calculateRightError()))
roomba.stop()

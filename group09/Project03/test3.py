from State import State
import time

# Default speed for the roomba
positive_velocity = 170

button = False

#Set point varibale
set_point= 13

# Constants for gains
KP =  1
KD =  .2

#Sampling  Time
sampling_time= .005

#target = 45

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
	
	#def wallFollow(self):
	    #while True:

	def calculateLeftError(self):
	    return self.State.readLeftBumper() - set_point

	def calculateRightError(self):
	    return self.State.readRightBumper() - set_point
	
	def calculatePController(self):
	    return KP*(self.calculatedLeftError())

	def calculatedDController(self):
	    return KD*(self.calculatedLeftError()/sampling_time)

roomba = test()
button = False
while True:
	time.sleep(1)
	#print ("Left Error Expected: {}".format(roomba.State.readLeftBumper() - set_point))
	#print("Left Error Recieved: {}".format(roomba.calculateLeftError()))
	print("Right Error Expected: {}".format(roomba.State.readRightBumper() - set_point))
	print("Right Error Recieved: {}".format(roomba.calculateRightError()))
roomba.stop()

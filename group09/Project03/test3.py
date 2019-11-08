from State import State
import time

# Default speed for the roomba
positive_velocity = 170

button = False

# Constants for gains
KP =  .02
KD =  20

target = 45

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
	
	def wallFollow(self):
	    while True:
		   	        	    

roomba = test()
button = False
roomba.drive()
time.sleep(3)
roomba.stop()

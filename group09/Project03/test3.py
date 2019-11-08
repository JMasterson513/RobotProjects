from State import State

# Default speed for the roomba
positive_velocity = 170

button = False

class test:
	
	def __init__(self):
	    self.State = State()
	    self.State.state(128)
	    self.State.state(131)
	
	def drive(self):
	    self.State.driveDirect(positive_velocity, positive_velocity)
	
	def readButton(self):
            global button
            button_state = self.State.readButton()
            if(button_state):
                button = not button

	def wallFollow(self):
            while True:
                self.readButton()
                print "not hello"
                while button:   
                    self.readButton()
	            print "hello"

roomba = test()
button = False
roomba.wallFollow()


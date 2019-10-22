from RoombaControl import RoombaControl

# Opcode for passive mode 
passive = 128

# Opcode for safe mode
safe = 131

# optimal sleep time after reading a command
sleep = 0.0125

# Velocity
velocity_left = 150
velocity_right = 150

def RandomWalk:

class RandomWalk: 
  
    # Initializes the connection and sets robot in safe and passive modes
    def __init__(self):
        self.Control = RoombaControl()
        self.Control.state(passive)
        self.Control.state(safe)

    def Walk(self):
	
	global walk_run

	while True:
            self.Control.DriveDirect(velocity_left, velocity_right)
         # if roomba is stopped
        
        # if roomba is stopped
        
        # if none of the drops or cliffs are activated
        
        # once the clean button is pressed

        # move until obstacle

        # rotate 180 + small random angle - clockwise if bumper left, counter bumper right

        # repeat
    
    # Continually read the state of the button
 
    def readButton(self):
        
        # Global variable which switches depending on whether on the button has been hit
        global run

        # Loop the whole time checking the state of the button
        while True:
            time.sleep(sleep) # provides space between button presses so there is no double reading 
            button_state = bool(self.State.readState())
            if(button_state):
                run = not run # Switches between running and not running
    #Thread for the drop Sensor
    def readDrop(self):
	global drop_run
	
	while True:
	    drop_state = bool(self.State.readDrop())
	    if(drop_state):
		drop_run = not drop_run
		
    #Thread for the cliff Sensor
    def readCliff(self):
        global cliff_run
	
	while True:
	    cliff_state = bool(self.State.readDrop())
	    if(cliff_state):
	        cliff_run = not cliff_run


    def readButton(self):       
        global button
        while done:
            time.sleep(button_sleep)
            button_state = bool(self.State.readState())
            if(button_state):
                button = not button # Switches between running and not running

    def readDrop(self):
        global drop
        while done:
            drop_state = bool(self.State.readDrop())
            if(drop_state):
                drop = not drop

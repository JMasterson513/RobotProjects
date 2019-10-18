from RoombaControl import RoombaControl

# Opcode for passive mode 
passive = 128

# Opcode for safe mode
safe = 131

def RandomWalk:

    # Initializes the connection and sets robot in safe and passive modes
    def __init__(self):
        self.Control = RoombaControl()
        self.Control.state(passive)
        self.Control.state(safe)

    def Walk(self):
        drop_sensors = self.Control.readDrop()
        cliff_sensors self.Control.readCliff()

        
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
        while done:
            time.sleep(button_sleep) # provides space between button presses so there is no double reading 
            button_state = bool(self.State.readState())
            if(button_state):
                run = not run # Switches between running and not running
               

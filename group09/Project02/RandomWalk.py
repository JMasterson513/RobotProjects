from RoombaControl import RoombaControl

# Opcode for passive mode 
passive = 128

# Opcode for safe mode
safe = 131

class RandomWalk:
    # Initializes the connection and sets robot in safe and passive modes
    def __init__(self):
        self.Control = RoombaControl()
        self.Control.state(passive)
        self.Control.state(safe)

    def Walk(self):
        
        # if roomba is stopped
        
        # if none of the drops or cliffs are activated
        
        # once the clean button is pressed

        # move until obstacle

        # rotate 180 + small random angle - clockwise if bumper left, counter bumper right

        # repeat
    
    # Continually read the state of the button
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
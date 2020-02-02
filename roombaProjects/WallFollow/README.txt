Project 2:
A python 2.7 program to connect to an iRobot Create 2 robot and make it follow a wall using a PD Controller. The progam should start and stop when the clean bbutton is pressed.

Interface.py:
Establishes a connection to the roomba
Allows user to send and recieve messages from the roomba
CLoses the connection to the roomba

State.py:
Sends a command to set the state of the roomba
Reads the state of the button and returns a value if the button is pressed
Drive method for controller the velocity of each wheel
Read IR Bump sensors and returns the vslue of the senesor
Puts robot in passive and safe mode

WallFollow.py:
Sets the roomba to drive and follow the roomba using a PD Controller.
Starts driving once the button is pressed and stops once the button is pressed

Installation:
Download the repository by cloning the repository:
    git clone https://github.com/JMasterson513/CSCE274.git
Ensure that you are using python 2.7
Make sure to have serial, threading, struct and time packages downloaded

Execution:
Use python 2.7 and call WallFollow.py
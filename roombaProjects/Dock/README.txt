Project 4:
A python 2.7 program to connect to an iRobot Create 2 robot and make it follow a wall until it 
finds a dock and then charge the robot.

Interface.py:
Establishes a connection to the roomba
Allows user to send and receive messages from the roomba
Closes the connection to the roomba

State.py:
Sends a command to set the state of the roomba
Reads the state of the button and returns a value if the clean button is pressed
Drive method for controller the velocity of each wheel
Read Light Bump sensors and returns the value of the sensor
Reads the omni-directional infrared sensor and returns a the value
Checks the charging state of the robot

RoombaGo.py:
Sets the roomba to drive and follow a wall using a PD Controller
When it finds a dock, initiates docking behavior approaching from either the side or front

Installation: 
Download the repository by cloning the repository:
    git clone https://github.com/JMasterson513/CSCE274.git
Ensure that you are using python 2.7
Make sure to have serial, threading, struct, time, and math packages downloaded

Execution:
Use python 2.7 and call RoombaGo.py
May need to reset the robot and disconnect all cords in order to reset the sensors

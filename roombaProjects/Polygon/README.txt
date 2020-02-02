Project 1:
A python 2.7 program to connect to an iRobot Create 2 robot and make it drive any regular polygon
starting and stopping when the clean button is hit.

Interface.py :
Establishes a connection to the roomba
Allows user to send and receive messages from the roomba
Closes the connection to the roomba

State.py :
Sends a command to set the state of the roomba
Reads the state of the button and returns the value corresponding to the pressed button
Puts the robot in drive mode taking in a velocity in mm/s and a radius in mm

PolygonDrive.py :
Makes the roomba drive a regular polygon of N sides and perimeter of 2m at a velocity of 170 mm/s

Installation : 
Download the repository by cloning the repository: 
    git clone https://github.com/JMasterson513/CSCE274.git
Ensure that you are using python 2.7
Make sure to have serial, threading, struct, and time packages downloaded

Execution:
Use python 2.7 and call PolygonDrive.py
To change the number of sides of the polygon, change sides variable defined at the start of the file




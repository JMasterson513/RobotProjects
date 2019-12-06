# Copyright 2019 Cassidy Carter, Joseph Masterson, and Alfred Stephenson II

from State import State
import time

#constant velocity
velocity = 170

#ir setpoint
ir_setpoint = 172

#wall setpoint
wall_set = 300

#error list
wall_list = [0]

#sleep time
sleep_time = 0.035

#PD Controller Constants
KP = 1
KD = .2

class findIR:
    def __init__(self):
        self.State = State()
        self.State.state(128)
        self.State.state(131)

    def drive(self):
        self.State.driveDirect(velocity, velocity)
    
    def Stop(self):
        self.State.driveDirect(0,0)
    
    def WallError(self):
        error = self.State.readRightBumper() - wall_set
        wall_list.append(error)

    def WallController(self):
        time.sleep(sleep_time)
        self.newErrorCalc()
        U_p = KP * (wall_list[-1])
        U = U_p + U_d
        return U

    def readCenterWall(self):
        wall = self.State.readCenterBumper()
        if(wall > 300):
            return True
        return False

    def centerWall(self):
        wall = self.readCenterWall()
        if(wall):
            time.sleep(.1)
            self.State.driveDirect(170,-170)
            time.sleep((math.radians(45))/(((170*2)/235)))

    def WallFollow(self):
        while True:
            U_current = self.PDController()
            wall = self.State.readCenterBumper()
            print("Wall Current {}".format(U_current))
            print("Center State {}".format(wall))
            self.centerWall()
            if(U_current  < 0):
                self.State.driveDirect(-170,170)
                time.sleep(sleep_time)
            elif(U_current > 0):
                self.State.driveDirect(170,-170)
                time.sleep(sleep_time)
            self.drive()

    def readCenterDock(self):
        wall = self.State.readCenterBumper()
        print("Wall State {}".format(wall))
        if(wall > 240):
            return True
        return False

    def chargingState(self):
        charge = roomba.State.isBatteryCharge()
        return bool(charge)

    def IRerrorCalc(self):
        error = self.State.readIROmni() - ir_setpoint
        error_list.append(error)
    
    def DockController(self):
        time.sleep(sleep_time)
        self.IRerrorCalc()
        Up = KP * (error_list[-1])
        Ud = KD * (error_list[-1] - error_list[-2])
        return Up + Ud

    def DockDrive(self):
        while True:
            U_current = self.DockController()

roomba = findIR()
while True:
    #print("Center Bump {}".format(roomba.readCenterDock()))
    state = roomba.State.readIROmni()
    print("IR State {}".format(state))
    #if(roomba.readCenterDock() == True):
        #print("Read a Center Bumper")
        #roomba.State.driveDirect(30,30)
        #time.sleep(0.05)
    if(state == 168):
        print("Turn left")
        roomba.State.driveDirect(100, 0)
        time.sleep(0.01)
    elif(state == 164):
        print("Turn right")
        roomba.State.driveDirect(0, 100)
        time.sleep(0.01)
    elif(state == 172):
        while(state == 172):
            roomba.State.driveDirect(100, 100)
            break
            #time.sleep(0.05)
    elif(roomba.State.isBatteryCharge() == 2):
        roomba.State.driveDirect(0,0)
        break
        #print("We are Charging")
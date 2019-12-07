# Copyright 2019 Cassidy Carter, Joseph Masterson, and Alfred Stephenson II

from State import State
import time
import math

#constant velocity
velocity = 170

#wall setpoint
wall_set = 400

#error list
wall_list = [0, 0]

#sleep time
sleep_time = 0.035

# Time bettwen each sample in the controller
sampling_time = 0.085

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
        wall_reading = self.State.readRightBumper()
        error = wall_reading - wall_set
        wall_list.append(error)

    def WallController(self):
        time.sleep(sleep_time)
        self.WallError()
        if(wall_list[-1] == -1 * wall_set):
            return -1 * wall_set
        U_p = KP * (wall_list[-1])
        U_d = KD * ((wall_list[-1] - wall_list[-2]) / sampling_time)
        U = U_p + U_d
        if(U < 0):
            return -1 * math.sqrt(-1 * U)
        return math.sqrt(U)

    def WallFollow(self):
        state = self.State.readIROmni()
        while(state <= 150):
            print("IR State in Wall Follow {}".format(state))
            U_current = self.WallController()
            while(U_current == -400):
                self.State.driveDirect(0, 100)
                U_current  = self.WallController()
            self.State.driveDirect(100 + U_current, 100)
            state = self.State.readIROmni()
        self.whichSide()

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

    def Dock(self):
        while True:
            state= self.State.readIROmni()
            print("IR State{} ".format(state))
            if(self.State.isBatteryCharge() ==2):
                self.State.driveDirect(0,0)
            elif(state==168):
                print("Turn Left")
                self.State.driveDirect(90,0)
                time.sleep(0.01)
            elif(state ==164):
                print("Turn Right")
                self.State.driveDirect(0,90)
                time.sleep(0.01)
            elif(state ==172):
                while(self.State.readIROmni() ==172):
                    self.State.driveDirect(100,100)
                    time.sleep(0.05)
                    if(self.State.isBatteryCharge()==2):
                        self.State.driveDirect(0,0)
                        self.Play()
                        break

    def Play(self):
        self.State.state(132)
        print("stuff")
        self.State.Play(1)
        self.State.state(128)
        self.State.state(131)

    def turn(self):
        angle = math.radians(135)
        omega = (2 * 170) / 235.0
        turn_sleep = (angle / omega)
        self.State.driveDirect(-170, 170)
        time.sleep(turn_sleep)
    
    def sideDock(self):
        self.State.driveDirect(250,200)
        time.sleep(2.5)
        self.State.driveDirect(0,0)
        time.sleep(.5)
        self.turn()
        self.State.driveDirect(0, 0)
        self.Dock()

    def whichSide(self):
        state = self.State.readIROmni()
        print(state)
        if(state == 161):
            self.sideDock()
        else:
            self.Dock()
    
    def FollowAndDock(self):
        self.WallFollow()
        self.whichSide()
    

roomba = findIR()
roomba.WallFollow()

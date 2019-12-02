from State import State
import time

#constant velocity
velocity = 170

#ir setpoint
ir_setpoint = 0

#error list
error_list = [0]

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

    def IRerrorCalc(self):
        error = self.State.readCenterBumper() - ir_setpoint
        error_list.append(error)
    
    def DockController(self):
        time.sleep(sleep_time)
        self.IRerrorCalc()
        Up = KP * (error_list[-1])
        Ud = KD * (error_list[-1] - error_list[-2])
    
    def Stop(self):
        self.State.driveDirect(0,0)

roomba = findIR()
while True:
    state = roomba.State.readIROmni()
    print state
    #if(roomba.State.readCenterBumper()):
        #print roomba.State.readCenterBumper()
        #roomba.Stop()
        #continue
    if(state == 168):
        roomba.State.driveDirect(170, 180)
    elif(state == 164):
        roomba.State.driveDirect(180, 170)
    elif(state == 161):
        roomba.State.driveDirect(170,170)
    elif(roomba.State.readCenterBumper()):
        print roomba.State.readCenterBumper()
        roomba.Stop()
        continue
        

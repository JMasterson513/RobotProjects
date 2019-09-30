from State import State
import time

roomba = State()

roomba.State.drive(100, 0)
time.sleep(5)
roomba.State.drive(100, 1)
time.sleep(3)
roomba.State.drive(100, 0)
time.sleep(5)


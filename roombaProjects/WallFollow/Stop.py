from State import State

class Stop:
    def __init__(self):
        self.State = State()

    def reset(self):
        self.State.state(7)

roomba = Stop()
roomba.reset()

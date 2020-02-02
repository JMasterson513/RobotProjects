# Copyright 2019 Joe Masterson, Cassidy Carter, and Alfred Stephenson II

from State import State

class Stop:
    def __init__(self):
        self.State = State()

    def passive(self):
        self.State.state(131)

roomba = Stop()
roomba.passive()

# Copyright 2019 Joe Masterson, Cassidy Carter, and Alfred Stephenson II

import Interface.py as Interface
import struct

clean = 0

class State:
    def __init__(self):
        Interface.open()
    
    def state(self, state):
        Interface.send(chr(state))
        
   
        


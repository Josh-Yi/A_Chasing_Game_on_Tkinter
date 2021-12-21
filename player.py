import numpy as np
class player:
    def __init__(self, location, speed=0):
        self.loc = location
        self.speed = speed

    def move(self, x):
        self.loc[0] = x[0] + self.loc[0]
        self.loc[1] = x[1] + self.loc[1]

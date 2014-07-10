import math

class Line(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

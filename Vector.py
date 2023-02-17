import math

# class of vector
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    #vector addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def normalize(self):
        length = math.sqrt(self.x * self.x + self.y * self.y)
        self.x = self.x / length
        self.y = self.y / length
        return self
    

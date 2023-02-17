# class point x and y coordinates
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __lt__(self, other):
        return self.x < other.x or self.y < other.y

    # vector addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # vector subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
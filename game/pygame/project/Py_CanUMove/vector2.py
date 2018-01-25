import math

class vect(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s,%s)"%(self.x,self.y)

    @classmethod
    def pointer(cls, p1, p2):
        return cls(p2[0]-p1[0], p2[1]-p1[1])

    def magnitude(self):
        return math.sqrt(self.x**2, self.y**2)

    def normalize(self):
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag

    def __add__(self, rhs):
        return vect(self.x + rhs.x, self.y + rhs.y)
    def __sub__(self, rhs):
        return vect(self.x - rhs.x, self.y - rhs.y)
    def __mul__(self, scalar):
        return vect(self.x * scalar, self.y * scalar)
    def __div__(self, scalar):
        return vect(self.x / scalar, self.y / scalar)

vector1 = vect()
print vector1
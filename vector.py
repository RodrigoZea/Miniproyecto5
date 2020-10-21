import math
import random

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def random(self, a=1):
        self.x = int(random.random() * a)
        self.y = int(random.random() * a)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dir_to(self, other):
        new_v = Vector(other.x - self.x, other.y - self.y)
        return new_v.normal()

    def normal(self):
        m = self.magnitude()
        return Vector(self.x / m, self.y / m)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def angle(self, other):
        dot = self.x * other.x + self.y * other.y
        
        return math.acos(dot / (self.magnitude() * other.magnitude()))

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def scalar_mult(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
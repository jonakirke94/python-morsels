import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('radius cannot be negative')
        self._radius = value

    @property
    def area(self):
        return (self.radius * self.radius) * math.pi

    def __repr__(self):
        return f'Circle({self.radius})'



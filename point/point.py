class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __sub__(self, another_point):
        return Point(self.x - another_point.x, self.y - another_point.y, self.z - another_point.z)

    def __add__(self, another_point):
        return Point(self.x + another_point.x, self.y + another_point.y, self.z + another_point.z)

    def __mul__(self, scale):
        return Point(self.x * scale, self.y * scale, self.z * scale)

    def __rmul__(self, scale):
        return Point(self.x * scale, self.y * scale, self.z * scale)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z


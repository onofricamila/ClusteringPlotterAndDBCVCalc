import math


class Circle():

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


    def area(self):
        return self.radius ** 2 * 3.14


    def perimeter(self):
        return 2 * self.radius * 3.14


    def contains(self, circle):
        distance_squared = math.sqrt(
            (circle.center[0] - self.center[0]) ** 2 +
            (circle.center[1] - self.center[1]) ** 2)
        return self.radius  > (distance_squared + circle.radius)

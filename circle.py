class Circle():

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


    def area(self):
        return self.radius ** 2 * 3.14


    def perimeter(self):
        return 2 * self.radius * 3.14

    def get_center(self):
        return self.center

    def get_radius(self):
        return self.radius

    def contains(self, circle):
        distance_squared = (circle.get_center()[0] - self.get_center()[0]) ** 2 + (
                    circle.get_center()[1] - self.get_center()[1]) ** 2
        return self.radius  >= (distance_squared + circle.get_radius())

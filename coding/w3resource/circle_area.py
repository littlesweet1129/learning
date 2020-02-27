# Write a Python program which accepts the radius of a circle 
# from the user and compute the area
import math
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_circle_area(self):
        self.area = math.pi * self.radius ** 2
        print('r = {}'.format(self.radius))
        print('Area = {}'.format(self.area))

radius = input('input radius of circle:')
circle = Circle(float(radius))
circle.get_circle_area()

# shapes/circle.py  — uses a RELATIVE import to reach sibling module utils
from .utils import PI, _describe


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

    def __repr__(self):
        return _describe("Circle", radius=self.radius)

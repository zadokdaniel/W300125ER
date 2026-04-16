# shapes/rectangle.py  — also uses relative import
from .utils import _describe


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return _describe("Rectangle", width=self.width, height=self.height)

import math

class Shape:
    """Base class for all shapes."""
    def area(self):
        raise NotImplementedError("The area() method must be overridden in derived classes.")

class Rectangle(Shape):
    """Represents a rectangle shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Represents a circle shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)

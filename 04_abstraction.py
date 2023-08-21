"""Abstraction is a key concept in Object-Oriented Programming (OOP) that involves simplifying complex reality by modeling classes based on the problem's requirements. It allows you to focus on the essential attributes and behaviors of an object while hiding unnecessary details."""
from abc import ABC, abstractmethod

# Abstract base class using ABC (Abstract Base Class)
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_area(self):
        pass

# Concrete classes inheriting from Shape
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Creating instances and using abstraction
circle = Circle("Circle", 5)
rectangle = Rectangle("Rectangle", 4, 6)

shapes = [circle, rectangle]

for shape in shapes:
    print(f"Shape: {shape.name}")
    print(f"Area: {shape.calculate_area()}\n")
    
"""We have an abstract base class 'Shape' defined using the 'ABC; module. It includes an abstract method 'calculate_area', which is marked with the '@abstractmethod' decorator. An abstract method is a method that is declared in the base class but does not have an implementation.

Two concrete classes, 'Circle' and 'Rectangle', inherit from the 'Shape' class. These classes provide specific implementations of the 'calculate_area' method.

We create instances of the 'Circle' and 'Rectangle' classes, representing specific shapes."""

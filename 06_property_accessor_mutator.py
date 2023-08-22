"""Properties: Properties provide a way to access class attributes as if they were regular instance variables, while allowing you to add custom behavior when accessing or modifying the attribute. Properties are defined using the '@property' decorator.

Accessors (Getters): Getters are methods that provide controlled access to attributes. They are used to retrieve the value of an attribute. Accessors are also defined using the '@property' decorator.

Mutators (Setters): Setters are methods used to set the value of an attribute. They provide controlled modification of the attribute value. Setters are defined using the '@<attribute_name>.setter' decorator."""

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print("Getting radius value")
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            print("Setting radius value")
            self._radius = value
        else:
            print("Invalid radius value")

    @property
    def area(self):
        return 3.14 * self._radius ** 2

# Creating a Circle instance
circle = Circle(5)

# Using the getter for radius
print("Radius:", circle.radius)

# Using the setter for radius
circle.radius = 7
print("Updated Radius:", circle.radius)

# Attempting to set an invalid radius
circle.radius = -2

# Using the property for area
print("Area:", circle.area)


"""The 'Circle' class has a private attribute '_radius' that is accessed and modified using properties, getters, and setters.

The '@property' decorator is used to define the getter for the 'radius' attribute. When 'circle.radius' is accessed, the 'radius' method is called.

The '@<attribute_name>.setter' decorator is used to define the setter for the 'radius' attribute. When 'circle.radius = value' is used, the 'radius' method is called with the assigned value.

The 'area' attribute is defined using a property, which calculates the area based on the '_radius' attribute."""
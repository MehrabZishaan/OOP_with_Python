"""
A class is like a blueprint or template for creating objects, and an object is an instance of a class. Each object has its own state (attributes) and behavior (methods).

To define a class in Python, you use the class keyword followed by the class name. Let's create a simple class called 'Car' as an example: """

class Car:
    """
    Now, let's add some attributes (data) to our 'Car' class. Attributes are defined within the class body and are accessed using the self keyword, which represents the instance of the class.
    """
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    """
    Here, we've added an __init__ method, which is a special method called a constructor. It is invoked automatically when an object is created from the class. The self parameter refers to the instance of the class, and we use it to assign values to the "brand", "model" and "year" attributes.

    Next, let's add a method (behavior) to our "Car" class. Methods are functions defined within a class and can perform various actions or calculations.
    """

    def start_engine(self):
        self.is_running = True
        print(f"The {self.brand} {self.model}'s engine is now running.")

    def stop_engine(self):
        self.is_running = False
        print(f"The {self.brand} {self.model}'s engine has been stopped.")

    def honk(self):
        if self.is_running:
            print("Beep beep!")
        else:
            print("The engine is not running. Start the engine first.")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2021)

# Accessing attributes
print(car1.brand)   # Output: Toyota
print(car2.model)   # Output: Accord
print(car1.year)    # Output: 2022

# Calling methods
car1.start_engine() # Output: The Toyota Camry's engine is now running.
car2.honk()         # Output: The engine is not running. Start the engine first.
car1.honk()         # Output: Beep beep!

car2.start_engine() # Output: The Honda Accord's engine is now running.
car2.honk()         # Output: Beep beep!

car1.stop_engine()  # Output: The Toyota Camry's engine has been stopped.
car1.honk()         # Output: The engine is not running. Start the engine first.

"""
We create two instances of the 'Car' class, 'car1' and 'car2', with different attributes. We then access their attributes (brand, model, year) using dot notation. We call the methods (start_engine, honk, stop_engine) on the car objects, and the methods perform actions based on the object's attributes.
"""
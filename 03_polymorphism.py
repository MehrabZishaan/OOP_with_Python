"""
Polymorphism is the ability of a class to take on multiple forms. In the context of OOP, it allows different classes to be treated as instances of a common parent class, and methods can be overridden in the child classes to provide different implementations.
"""
class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

class Cat(Animal):
    def speak(self):
        print("Cat meows.")

def animal_sound(animal):
    animal.speak()

# Create instances of different classes
animal = Animal()
dog = Dog()
cat = Cat()

# Demonstrate Polymorphism
animal_sound(animal)  # Output: Animal speaks.
animal_sound(dog)     # Output: Dog barks.
animal_sound(cat)     # Output: Cat meows.

"""
In this code, we have a parent class 'Animal' with a 'speak' method, and two child classes 'Dog' and 'Cat' that override the 'speak' method with their own implementations.

The 'animal_sound' function demonstrates polymorphism. It takes an argument 'animal', which is an instance of the 'Animal' class. When the 'speak' method is called on the 'animal' object inside the function, the specific implementation of the method depends on the actual type of the object passed.
"""

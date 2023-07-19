# Single Inheritance involves a child class inheriting from a single parent class.
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    def bark(self):
        print("Woof woof!")


# Multiple Inheritance involves a child class inheriting from multiple parent classes.
class Flyable:
    def fly(self):
        print("Flying...")


class Bird(Animal, Flyable):
    def chirp(self):
        print("Chirp chirp!")


# Multilevel Inheritance involves a chain of inheritance with multiple levels of parent-child relationships.
class Mammal(Animal):
    def give_birth(self):
        print(f"{self.name} is giving birth.")


class Dolphin(Mammal):
    def swim(self):
        print(f"{self.name} is swimming.")


# Hierarchical inheritance involves multiple child classes inheriting from a single parent class.
class Cat(Animal):
    def meow(self):
        print("Meow meow!")


class Lion(Animal):
    def roar(self):
        print("Roar!")


# Create instances and demonstrate inheritance

# Single Inheritance
dog = Dog("Buddy")
dog.eat()   # Output: Buddy is eating.
dog.bark()  # Output: Woof woof!

print()

# Multiple Inheritance
bird = Bird("Sparrow")
bird.eat()  # Output: Sparrow is eating.
bird.chirp()  # Output: Chirp chirp!
bird.fly()  # Output: Flying...

print()

# Multilevel Inheritance
dolphin = Dolphin("Dolphie")
dolphin.eat()       # Output: Dolphie is eating.
dolphin.give_birth()  # Output: Dolphie is giving birth.
dolphin.swim()      # Output: Dolphie is swimming.

print()

# Hierarchical Inheritance
cat = Cat("Whiskers")
cat.eat()   # Output: Whiskers is eating.
cat.meow()  # Output: Meow meow!

lion = Lion("Simba")
lion.eat()  # Output: Simba is eating.
lion.roar()  # Output: Roar!

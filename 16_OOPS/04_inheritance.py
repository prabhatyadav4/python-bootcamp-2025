# Base class Animal
class Animal:
    country = "Australia"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

    def speak(self):
        print("Speaking...")  # Base class method

# Derived class Dog inheriting from Animal
class Dog(Animal):
    def speak(self):
        super().speak()  # Call the base class method
        print("Woof!")  # Additional behavior for Dog

# Create an instance of Dog
d = Dog("Bruno")
d.speak()  # Call the speak method
print(d.country)  # Access the class attribute from the base class
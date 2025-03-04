"""
OOP is a programming paradigm based on objects that contain data (attributes) and functions (methods).

Class - blueprint for creating objects
Object - an instance of a class
"""

class Car:
    #__init__ - constructor that initializes attributes when an object is created
    def __init__(self, brand, model, year):
        #self - refers to the current instance of the class
        self.brand = brand #instance variable
        self.model = model
        self.year = year

    def start_engine(self):
        #start_engine() is a method that acts on the object's attributes
        return f"{self.brand} {self.model}'s engine started!"
    
    #creating objects (instances)
car1 = Car("Toyota", "C
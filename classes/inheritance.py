#Inheritance allows a class to inherit properties and methods from another class

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

class ElectricCar(Car): #inheriting from Car
    def __init__(self, brand, model, year, battery_size):
        # super().__init__() calls the parent class-s constructor
        super().__init__(brand, model, year) #Call parent class constructor
        self.battery_size = battery_size #new attribute

    #adds a new method
    def charge_battery(self):
        return f"{self.brand} {self.model} is charging with a {self.battery_size} kWh battery."
    
#Creating an ElectricCar instance
nissan = ElectricCar("Nissan", "Aryia", 2024, 100)

print(nissan.charge_battery())

#Method overriding

#A subclass can override a parent method to change its behavios
class ElectricCar(Car):
    def start_engine(self): #overriding method
        return f"{self.brand} {self.model} starts silently with an electric motor."
    
tesla = ElectricCar("Tesla", "Model S", 2023)
print(tesla.start_engine())
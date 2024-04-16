# Class

class Car:
    #constructor
    def __init__(self, _color, _make): # Can use underscores e.g. _color to indicate to developers that it's a private attribute without changing the code
       self._color = _color
       self._make = _make
    
    # Getters (Accessors)
    def get_color(self):
        return self._color
    
    # Setters (Mutators)
    def set_color(self, _color):
        # if/else condition can be applied here before setting attributes
        self._color = _color

    def run(self):
        print(f"{self._make} is running! VROOM VROOM!")

my_car = Car("White", "Honda")

print(my_car._color)
print(my_car._make)
my_car.run() # This will execute the run method, without having to type "print"

my_car.set_color = "Red" # Can to this to amend attribute


your_car = Car("Black", "BMW")
print(your_car._color)
print(your_car._make)
your_car.run()



# Inheritance

class PetrolCar(Car): # Car will be the parent class
    def __init__(self, color, make, capacity_of_tank): # Can have the same attributes but can add some also
        super().__init__(color, make) # .super() is used to inherit existing attributes from part class
        self.capacity_of_tank = capacity_of_tank

    def get_capacity(self):
        return self.capacity_of_tank


my_petrol_car = PetrolCar("silver", "toyota", 50)
my_petrol_car.run() # This was defined in the parent class but can still be used in the inherited class
print(my_petrol_car.get_capacity())


class ElectricCar(Car): # We can use "pass" to leave empty, but pass "Car" as argument --> this class will now be an exact copy of parent class
    pass
    # Overriding -- an example of polymorphism
    def run(self):
        print("This car is silent! No Vrooming shhhh")

my_electric_car = ElectricCar("Beige", "Moto")
print(my_electric_car._color)
my_electric_car.run() # Will run override



# Abstraction

# Any class that inherits from an abstract class must implement the @abstractmethod 

from abc import ABC, abstractmethod

class Meal(ABC):

    @abstractmethod
    def requiredCutlerty(self):
        pass

class fingerFood(Meal):
    pass
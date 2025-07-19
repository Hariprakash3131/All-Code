# Hierarchical Inheritance
# Multiple child classes inherit from a single parent class

# Parent class
class vehicle:
    no_of_wheels = 4  # Common property for all vehicles

    def moveForward(self):
        # Common behavior for all vehicles
        print("Vehicle is moving forward")

# Child class 1 inheriting from vehicle
class car(vehicle):
    no_of_airbags = 5  # Specific to car

# Child class 2 inheriting from vehicle
class bike(vehicle):
    mileage = 35  # Specific to bike

# Creating object of car class
c = car()
print(c.no_of_wheels)     # Inherited from vehicle class → Output: 4
print(c.no_of_airbags)    # Specific to car → Output: 5
c.moveForward()           # Inherited method from vehicle → Output: Vehicle is moving forward

# Creating object of bike class
b = bike()
print(b.mileage)          # Specific to bike → Output: 35
print(b.no_of_wheels)     # Inherited from vehicle → Output: 4
b.moveForward()           # Inherited method → Output: Vehicle is moving forward

# Printing return value of moveForward() (which is None, since it only prints)
print(b.moveForward())    # Output: Vehicle is moving forward (and then prints None)

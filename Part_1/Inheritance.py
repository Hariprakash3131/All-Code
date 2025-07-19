# Inheritance
#Single Inheritance
#One child class inherit form one parent class 
# Inheritance allows reusability of code by letting one class (child)
# inherit properties and methods from another (parent)

# Parent class (Base class)
class vehicle:
    no_of_wheels = 4  # Class variable

    def moveForward(self):
        # Method to simulate vehicle movement
        print("Vehicle is moving forward")

# Child class (Derived class) inheriting from vehicle
class car(vehicle):
    no_of_airbags = 5  # Additional property specific to car

# Creating object of child class car
c = car()

# Accessing inherited property from vehicle class
print(c.no_of_wheels)    # Output: 4

# Accessing property from car class
print(c.no_of_airbags)   # Output: 5

# Accessing inherited method from vehicle class
c.moveForward()          # Output: Vehicle is moving forward

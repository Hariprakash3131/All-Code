#Constructor
class car:
    def __init__(self):
        print("This is a Constructor!")
        self.number_of_wheels = 4
        self.milage = 20
        self.number_of_airbags = 5

    def moveForward(self,speed):
        print("car is moving with a speed",speed)

    def moveBackward(self):
        print("car is moving backward")

c = car()   #Instance of a class - Object Instantiation 
print(c.number_of_airbags)  
print(c.milage)            
c.moveBackward()             

c1 = car() 
c1.milage=25 
print(c1.number_of_airbags)  
print(c1.milage)            
c.moveForward(100)             

#Output
"""
This is a Constructor!
5
20
car is moving backward
This is a Constructor!
5
25
car is moving with a speed 100
"""
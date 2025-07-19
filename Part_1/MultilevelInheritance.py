#Multi level Inheritance
#Grandfather -> Father -> Son
#A class inherits from a class which it self inherits from another class
class vehicle:
    no_of_wheels=4
    
    def moveForward(self):
        print("Vehicle is moving forward")
        
class car(vehicle):
    no_of_airbags=5

class tata(car):
    mileage=35
    
c=tata()
print(tata.no_of_wheels)  #4
print(tata.no_of_airbags) #5
print(tata.mileage)       #35
c.moveForward()           #Vehicle is moving forward


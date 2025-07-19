class car:      
    def __init__(self):                   #Constructor
        print("This is a Constructor!")
        self.number_of_wheels = 4
        self.milage = 20
        self.number_of_airbags = 5
        self.car_name="Tata"
    def __del__(self):
        print("This is a destructor",self)
    def __str__(self):
        return (self.car_name)

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

#Output:
"""
This is a Constructor!
5
20
car is moving backward
This is a Constructor!
5
25
car is moving with a speed 100
This is a destructor Tata
This is a destructor Tata
"""

#Output:

class bank_acc:
    def __init__(self,customer_name,balance,account_number):
        self.customer_name=customer_name
        self.balance=balance
        self.account_number=account_number
        
    def __str__(self):
        return (self.customer_name)
    
bank=bank_acc("Hari",4700,162931)
print(bank.customer_name,bank.balance,bank.account_number)
print(bank)
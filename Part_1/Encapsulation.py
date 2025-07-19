#Encapsulation
#Binding of variables and methods into a single unit (class)
#Getters and Setters for accessing and modifying private data
#It has Security aspect
#Encapsulation has three access types:
#1. Private: __ (double underscore)
#2. Protected: _ (single underscore)
#3. Public: default (no underscore)

class car:
    def __init__(self):
        print("This is a Constructor!")
        self.__customer_name = "hari"        # Private variable (double underscore)
        self.number_of_wheels = 4            # Public variable
        self.milage = 20                     # Public variable
        self.number_of_airbags = 5           # Public variable

    def moveForward(self, speed):
        # Public method to move car forward
        print("car is moving with a speed", speed)

    def moveBackward(self):
        # Public method to move car backward
        print("car is moving backward")
        
    # Getter method to access private variable
    def get_customer_name(self):
        return self.__customer_name
    
    # Setter method to modify private variable
    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

# Create object of class car
c = car()   

# Accessing private variable using getter
print(c.get_customer_name())        

# Accessing public attributes directly
print(c.number_of_airbags)          
print(c.milage)                      

# Calling public method
c.moveBackward()   

# Modifying private variable using setter
c.set_customer_name("James")

# Confirming the updated value using getter
print(c.get_customer_name())    

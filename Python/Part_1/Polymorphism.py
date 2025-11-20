# Polymorphism
# Poly - many, morph - forms
#It has two types 
#1.compile time
#2.Run Time

#Compile Time Polymorphism
class Summation:
    # Using default arguments to mimic method overloading
    def sum(self, a, b, c=0):
        return a + b + c

# Create object of the class
obj = Summation()

# Calling the method with different argument counts
print(obj.sum(1, 2))          # Two arguments
print(obj.sum(1, 2, 3))       # Three arguments
print(obj.sum(1.0, 5.0))      # Float values

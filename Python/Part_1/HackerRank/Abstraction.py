# It Has 2 types:
# 1. Abstract class
# 2. Abstract Method

# Importing abstract base class module
from abc import ABC, abstractmethod  # ABC -> Abstract Base Class

# Defining abstract base class
class Car(ABC):
    @abstractmethod  # Abstract method (must be implemented by subclasses)
    def moveForward(self):
        pass

    @abstractmethod
    def moveBackward(self):
        pass

    @abstractmethod
    def fm(self):
        pass

# Subclass Tata inherits from Car and implements all abstract methods
class Tata(Car):
    def moveForward(self):
        print("Tata is moving Forward")

    def moveBackward(self):
        print('Tata is moving Backward')

    def fm(self):
        print("Tata is playing fm")

# Subclass Tesla inherits from Car and implements all abstract methods
class Tesla(Car):
    def moveForward(self):
        print("Tesla is moving Forward")

    def moveBackward(self):
        print('Tesla is moving Backward')

    def fm(self):
        print("Tesla is playing fm")

# Creating an object of Tesla (valid because all abstract methods are implemented)
tesla = Tesla()
tesla.moveBackward()  # Output: Tesla is moving Backward

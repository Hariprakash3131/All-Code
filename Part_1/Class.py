class car:
    number_of_wheels = 4
    milage = 20
    number_of_airbags = 5

    def moveForward(self):
        print("car is moving")

    def moveBackward(self):
        print("car is moving backward")

c = car()   #Instance of a class - Object Instantiation 
print(c.number_of_airbags)  # Output: 5
print(c.milage)             # Output: 20
c.moveBackward()             # Output: "car is moving Backward"

c1 = car()
c1.milage = 25
print(c1.number_of_airbags) # Output: 5
print(c1.milage)    # Output: 25
c1.moveForward()


#Quiz
#Bank
class bank_acc():
    customer_name="Hari"
    balance=4700
    account_number=162931
    
bank=bank_acc()
print(bank.customer_name)
print(bank.balance)
print(bank.account_number)

bank1=bank_acc()
bank1.customer_name="James"
bank1.account_number=223144
print(bank1.customer_name)
print(bank1.balance)
print(bank1.account_number)
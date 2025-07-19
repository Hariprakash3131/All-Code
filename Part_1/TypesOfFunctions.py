#TypesOfFunction

#Void
#Non-Void 

#Void 
def add():
    a=int(input("Enter the a:"))
    b=int(input("Enter the b:"))
    print(a+b)  #Void function
    
sum1=add()
print(sum1)

def sub():
    c=int(input("Enter the c:"))
    d=int(input('Enter the d:'))
    return c+d  #Non-Void function You can return string float

sum2=sub()
print(sum2)
#Non-void function with argument and parameter
def add(a,b):#parameter
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b

a=int(input('Enter the a:'))
b=int(input('Enter the b:'))
add1=add(a, b)
print(add1)
sub1=sub(a, b)
print(sub1)
mul1=mul(a,b)
print(mul1)

#Quiz
def areaofrect(length,width):
    return length*width

rectangle=areaofrect(5,3)  #Arguments
print(rectangle)

<<<<<<< HEAD
#Recursion
#Recursion in Python is a programming technique where a
# function calls itself to solve smaller instances of the same problem
'''
def add(n):
    print(n)
    return add(n-1)
ans=add(5)

'''
def sum_n(n):
    #Base case
    if(n==1):
        return 1
    
    #Recursive case
    return n + sum_n(n-1)

print(sum_n(2))

#Quiz
def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

result=factorial(5)
=======
#Recursion
#Recursion in Python is a programming technique where a
# function calls itself to solve smaller instances of the same problem
'''
def add(n):
    print(n)
    return add(n-1)
ans=add(5)

'''
def sum_n(n):
    #Base case
    if(n==1):
        return 1
    
    #Recursive case
    return n + sum_n(n-1)

print(sum_n(2))

#Quiz
def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

result=factorial(5)
>>>>>>> cae182cc266dc1524d63f45e96830940a6d0ce61
print(result) 
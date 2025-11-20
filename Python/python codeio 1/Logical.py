#Logical operator
# or
# and
# not
a=10
b=5
s1=(a==10)
s2=(b==10)
print(s1 or s2)#True

a=5
b=5
s1=(a==5)
s2=(b==5)
print(s1 or s2)#True


# and
a=10
b=10
s1=(a==10)
s2=(b==10)
print(s1 and s2)#True


#not 
print(not(True))#false
print(not(False))#True

#Quiz
num=10
print(num>5 and num<15)     #True
print(num%2==0 or num%3==0) #True
print(not(num==0))          #True
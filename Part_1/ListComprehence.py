<<<<<<< HEAD
#List Comprehension

#Normal
arr=[1,2,3,4,5,6]
odd=[]
for i in arr:
    if i%2==1:
        odd.append(i)
print(odd)

#List Comprehension
odd=[i for i in arr]
print(odd)
odd=[i for i in arr if i % 2 ==1]
print(odd)

#even
even=[i for i in arr if i % 2==0]
print(even)

#normal
lst=[]
for i in range(1,101):
    lst.append(i)
print(lst)


#List comprehension
lst=[i for i in range(1,101)]
=======
#List Comprehension

#Normal
arr=[1,2,3,4,5,6]
odd=[]
for i in arr:
    if i%2==1:
        odd.append(i)
print(odd)

#List Comprehension
odd=[i for i in arr]
print(odd)
odd=[i for i in arr if i % 2 ==1]
print(odd)

#even
even=[i for i in arr if i % 2==0]
print(even)

#normal
lst=[]
for i in range(1,101):
    lst.append(i)
print(lst)


#List comprehension
lst=[i for i in range(1,101)]
>>>>>>> cae182cc266dc1524d63f45e96830940a6d0ce61
print(lst)
#Tuples
#Tuples is a Immutable

t=(1,2,4,5,6,7,8)
print(type(t))

#index Find
print(t[4])

#You can Redeclare
t=(1,2,3,4,5,6,6,7,8)
print(t)

#length
print(len(t))

#Min and Max
print(min(t))

print(max(t))

#count
print(t.count(6))

#index
print(t.index(4))

#Converted Tuples to List
lst=list(t)
print(type(lst))

#converted list to tuples
tup=tuple(lst)
print(type(tup))

#Weird Case
num=(9)
print(type(num)) #<class 'int'>

num=(9,)
print(type(num))

#Quiz
#Tuples allow Reassignment

fru=("apple","banana","Mango","kiwi","strawberry")
print(fru)

fru +=("grape",)

print(fru)
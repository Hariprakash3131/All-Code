#Set
#Set is a un ordered collection
#Set is a uniq values 
#Set does not allow duplicate values
set1={1,2,3,4,4,3}
print(set1)
print(type(set1))

#add a value
set1.add(99)
print(set1)

set1.add('1')
print(set1)

#remove
set1.remove(1)
print(set1)

#clear
set1.clear()
print(set1)

lst=[4,5,7,95]
set1.clear()
set2=set(lst)
print(set2)
lst=[1,2,3,4]

#Length of List
print(len(lst))

#Before Append add
print(lst)

#Append of List
lst.append(5)
print(lst)
 
#extend of list
lst1=[6,7,8]
lst.extend(lst1)
print(lst)

#insert of index
lst.insert(0,0)
print(lst)

#count of list
print(lst.count(3))

#index find list
print(lst.index(4))

#Min and Max
print(min(lst))
print(max(lst))

#sorting
#Reverse sorting
lst.sort(reverse=True)
print(lst)
#Acending Sorting 
lst.sort()
print(lst)

#Empty
#lst.clear()
#print(lst)

#Mutability
lst[0]=1000
print(lst)

#pop
lst.pop()
print(lst)

lst.pop(0)
print(lst)

#Remove
lst.remove(7)
print(lst)
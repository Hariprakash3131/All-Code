#Set Operators
set1={1,2,3,4}
set2={4,5,6}

#union
print(set1.union(set2))  #{1, 2, 3, 4, 5, 6}

#Intersection
print(set1.intersection(set2))# {4}

#Difference
print(set1.difference(set2)) #{1, 2, 3}

for i in set1: 
    print(i)
"""
1
2
3
4
"""
#membership
print(1 in set1)#True

print(1 in set2)#False

#Quiz
set1={1,2,3,4}
set2={4,5}
set3={2,3,4,5,7,8}
print(set1.union(set2).intersection(set3)) # {2, 3, 4, 5}
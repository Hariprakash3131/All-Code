#Dictionaries Function
#Un order 
map1={1:["one",(1,2)],2:"Two"}
print(map1)
print(type(map1))

#Accessing ,Get -map[1]
print(map1.get(1))

#length 
print(len(map1))

#Keys 
print(map1.keys())

#Values
print(map1.values())

#items
print(map1.items())

#insert
map1[4]="Three"
print(map1)  #{1: ['one', (1, 2)], 2: 'Two', 4: 'Three'}

map1[3]="Three"
print(map1)

#remove
map1.pop(3)
print(map1)

#clear
map1.clear()
print(map1)

#Create empty value dict
map1=dict()


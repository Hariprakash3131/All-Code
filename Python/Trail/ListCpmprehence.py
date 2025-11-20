#Write a list comprehension to generate a list of squares from 1 to 20.
lst=[]
squares =[lst**2 for lst in range(1,21)  ]
print(squares)

#Create a list of all even numbers between 1 and 100 using list comprehension.
even=[i for i in range(1,101) if i%2==0]
print(even)

#Generate a list of all numbers between 1 and 100 that are divisible by both 3 and 5.

div=[i for i in range(1,101) if i%3==0 and i%5==0]
print(div)

#Write a list comprehension to convert all strings in a list to lowercase.
upper_case=['HARI','JAMES','SOKER']
low=[i.lower() for i in upper_case ]
print(low)

#Use list comprehension to build a multiplication table of 5 up to 50.
table=[i*5 for i in range(1,11)]
print(table)




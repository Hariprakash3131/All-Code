#Unit Digit
'''
In Python, the unit digit (also known as the ones digit or last digit)
of a number is the rightmost digit in the number.
You can easily get it using the modulo operator (%).

✅ Explanation:

The % (modulo) operator gives the remainder when a number is divided by 10.
The remainder is always the last digit.

Let me know if you want to find the unit digit of a negative number or
for multiple numbers in a list!

'''
'''
Unit digit
num=int(input("Enter the number:"))
print(num%10)

'''
#Tength Digit
num=int(input("Enter the  number:"))
num=num//10
print(num%10)

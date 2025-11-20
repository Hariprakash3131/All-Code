# Python Output-based MCQs (Q51 - Q65)

print("Q51:", end=" ")
x = 5
y = 2
print(x ** y)  # Expected 25

print("Q52:", end=" ")
print("Hello" * 3)  # Expected HelloHelloHello

print("Q53:", end=" ")
print(type(5/2))  # Expected <class 'float'>

print("Q54:", end=" ")
print(10 // 3)  # Expected 3

print("Q55:", end=" ")
a = [1, 2, 3]
print(a[1:])  # Expected [2, 3]

print("Q56:", end=" ")
print(bool(0), bool(1))  # Expected False True

print("Q57:", end=" ")
print("Python"[::-1])  # Expected nohtyP

print("Q58:", end=" ")
print([1, 2] * 2)  # Expected [1, 2, 1, 2]

print("Q59:", end=" ")
x = "123"
print(int(x) + 5)  # Expected 128

print("Q60:", end=" ")
print(2 == 2.0)  # Expected True

print("Q61:", end=" ")
print(type([1,2]))  # Expected <class 'list'>

print("Q62:", end=" ")
a = (1, 2, 3)
try:
    a[0] = 5  # Tuples are immutable
except Exception as e:
    print("Error:", e)  # Expected Error

print("Q63:", end=" ")
a = {1, 2, 3, 2}
print(a)  # Expected {1, 2, 3}

print("Q64:", end=" ")
print("5" + "6")  # Expected "56"

print("Q65:", end=" ")
print(10 > 5 and 5 > 2)  # Expected True

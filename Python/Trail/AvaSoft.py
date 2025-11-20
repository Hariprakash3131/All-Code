print(type([]))
print(2**3**2)

a="hariprakash"
print(len(a))
b=bool([])
print(b)

def func(x, y=[]):
    y.append(x)
    return y

print(func(1))
print(func(2))

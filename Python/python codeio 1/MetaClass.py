# Define a metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name} with metaclass {cls.__name__}")
        dct['greeting'] = "Hello from metaclass!"
        return super().__new__(cls, name, bases, dct)

# Use the metaclass
class MyClass(metaclass=MyMeta):
    pass

print(MyClass.greeting)  # Hello from metaclass!


# ✅ In short:

# Classes create objects.

# Meta classes create classes.
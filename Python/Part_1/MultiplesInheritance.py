# Multiple Inheritance
# A class inherits from more than one parent class
"""
    ✅ Python’s Answer: MRO (Method Resolution Order)

Python uses the MRO to resolve this ambiguity. The child class looks at its parent classes from left to right, so:

    class child(father, mother) → Python takes hair_color from father ✅

    class child(mother, father) → Python takes hair_color from mother ✅
"""




# Parent class 1
class father:
    hair_color = "black"  # father's hair color

# Parent class 2
class mother:
    hair_color = "white"  # mother's hair color (same attribute as father)
    eye_color = "Blue"    # mother's eye color

# Child class inherits from both father and mother
# Order of inheritance determines which parent's hair_color is used
# If we write: class child(mother, father) → hair_color = white
# If we write: class child(father, mother) → hair_color = black (because father is listed first)

class child(father, mother):
    no_of_legs = 2  # specific to child

# Creating object of child
son = child()

# Accesses hair_color from the first parent in the inheritance list (father)
print(son.hair_color)    # Output: black

# Accesses eye_color from mother, as only mother has this attribute
print(son.eye_color)     # Output: Blue

# Accesses child's own attribute
print(son.no_of_legs)    # Output: 2

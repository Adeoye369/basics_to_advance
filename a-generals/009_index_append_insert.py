
pets = ["Cat", "Dog", "Mouse", "Babbit"]

# find index of mouse
print(pets.index("Mouse"))

# place at the back
pets.append("Hamster")
print(pets)

# place at the index specified, shift other value
pets.insert(0, "Parrot") # insert in first
print(pets)

pets.insert(3, "Monkey")
print(pets)



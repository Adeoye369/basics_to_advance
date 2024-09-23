

pets = ["Parrot","Cat", "Dog", "Mouse", "Babbit", "Hamster"]
print(pets)
# using remove() - specify name
pets.remove("Hamster")
print("remove('Hamster') - ", pets)

# using pop() - Specify index just like del
pets.pop(2)
print("pop(2) -            " , pets)

del pets[2]
print("del[2] -            ", pets)


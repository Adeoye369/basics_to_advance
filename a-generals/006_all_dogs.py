
dogs = []

while True:
    dogName = input("Your dog name :")

    if dogName == '': break

    # concatenate dog name
    dogs = dogs + [dogName]

print("Your Dog names are:")
for index, dog in enumerate(dogs):
    print(f"dog {index + 1} is {dog}")
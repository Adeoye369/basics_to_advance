
'''
FizzBuzz game:

Rules if the number is divisible by 3 print "Fizz", if by 5 print "Buzz" 
if divisible by 3 and 5, print "FizzBuzz"

Input the number between 100 - 500
'''

# Get user number:

try:
    number = int(input("Input number between 100 to 500:"))

    for i in range(1,number + 1):
        if (i % 3 == 0 and i % 5 == 0): print("FizzBuzz")
        elif (i % 3 == 0) : print("Fizz")
        elif (i % 5 == 0) : print("Buzz")
        else: print(f"{i}")

except ValueError:
    print(" The input value must be a number")
    
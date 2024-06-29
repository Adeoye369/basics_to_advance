import random

# Test Password string
passString = "rthglafsghglsf"

# Test numbers of symbols need
pass_sym_num = 3

# random symbols generated
rand_symbol = "%$@"


# this Check if the positioning of the symbol string will
# Exceed the index of the total password length
# In such case, try another random positon
found = False
while not found:
    # this is a string 
    i = random.randint(0, (len(passString) - 1))
    if((i + pass_sym_num) > len(passString)):
        print(f"X BAD pos: i + pass_sym num = {i + pass_sym_num}, len(passString) ={len(passString)}") 
        found = False
    else:
        print(f"! GOOD pos: i + pass_symbol = {i + pass_sym_num}, len(passString) ={len(passString)}")
        found = True 
    
passString = passString.replace(passString[i:i+pass_sym_num], rand_symbol)

print(f"Your new password is : {passString}")

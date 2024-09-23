'''
PyPassword Generator:
- It takes in the 'LENGTH' of password you want
- It will request for how many 'SYMBOLS' do you want inside
- And also how many 'NUMBERS' do you want inside.
'''
import random

def get_numbers_chars():
    return [chr(x) for x in range(48, 57+1)]

def get_symbols_chars():
    sym_chars = []
    sym_chars.extend([chr(x) for x in range(35, 38+1)])
    sym_chars.extend(['!','>','<', '?','@'])
    return sym_chars

def get_letters_chars():
    let_chars = []
    let_chars.extend([chr(x) for x in range(65, 91+1)])
    let_chars.extend([chr(x) for x in range(97, 122+1)])
    return let_chars


# Get the length of password:
pass_len = int(input("How many letters? "))

# Get the numbers of symbols
pass_sym_len = int(input("How many symbols: "))

# Get the numbers of 'numbers'
pass_num = int(input("How many numbers: "))

pass_chars = []
# Gen. random password
for p in range(0, pass_len):
    pass_chars += random.choice(get_letters_chars())

for s in range(0, pass_sym_len):
    pass_chars += random.choice(get_symbols_chars())

for n in range(0, pass_num):
    pass_chars += random.choice(get_numbers_chars())

random.shuffle(pass_chars)
pass_string = ''.join(pass_chars)
print(f"Your new password is : {pass_string}")

    
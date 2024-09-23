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

def generate_password():

    # Get the length of password:
    pass_letters_len = random.randint(8, 18)

    # Get the numbers of symbols
    pass_symbol_len = random.randint(2, 4)

    # Get the numbers of 'numbers'
    pass_number_len = random.randint(2, 4)

    pass_chars = []
    # Gen. random password
    pass_chars += [random.choice(get_letters_chars()) for _ in range(0, pass_letters_len)]
    pass_chars += [random.choice(get_symbols_chars()) for _ in range(0, pass_symbol_len)]
    pass_chars += [random.choice(get_numbers_chars()) for _ in range(0, pass_number_len)]

    # print(f"Pass char : {pass_chars}")

    random.shuffle(pass_chars)
    pass_string = ''.join(pass_chars)
    
    # print(f"Your new password is : {pass_string}")
    return pass_string

    
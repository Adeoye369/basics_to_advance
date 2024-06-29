alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

from art import ceaser_logo


# ceaser function 'encrpyt' and 'decrpyt' text
def ceasar(cipher_direction, input_text, shift_amount):

    cypher_text=""

    for letter in input_text:

        if not letter in alphabet: 
            cypher_text += letter
            continue

        position = alphabet.index(letter) 

        if cipher_direction == "decode": 
            new_position = position - shift_amount
            if(new_position < 0): # index in -ve
                new_position = (len(alphabet)) + new_position # go to end index

        elif cipher_direction == "encode":
            new_position = position + shift_amount
            if(new_position > len(alphabet)-1): # if index is out of range
                new_position = (new_position % (len(alphabet))) # circle back to begin index
            
        cypher_text += alphabet[new_position]
   
    print(f"The {cipher_direction}d text is <<{cypher_text}>>")



def main():
    print(ceaser_logo)

    terminal="Y"
    while(terminal != "N" ):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if(direction != "encode" and direction != "decode"):
            print(f"{direction} is not acceptable type 'encode' or 'decode'" )
            continue

        text = input("Type your message:\n").lower()

        shift = int(input("Type the shift number:\n"))
        if(shift > len(alphabet)-1): 
            print(f"direction too large, max is {len(alphabet)-1}")
            continue

        ceasar(direction, input_text=text, shift_amount=shift) 

        terminal= input("Type 'Y' to start or 'N' to exit:\n ").upper()
    
main()
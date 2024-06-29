
# Word list

import random

word_list = ["monkey", "kangaroo", "mouse", "sheep"]

# Randomly choose word from word_list
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
print(" Chosen word is ", chosen_word)

# Ask the user to guess a letter and assign 
# their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ")[0].lower()

# Check if he letter user guessed is in the chosen word
word_len = len(chosen_word)

# Create blanks as many as chosen words
display =[]
for _ in range(word_len):
    display += "_"

game_over = False
user_lives = 3

while not game_over:

    # Word completed, End Game display game won
    if(display == chosen_word ):
        game_over = True
        print("Game! Over, YOU WIN!!!🎉🎉🎉")

    # fill in the blanks for correct word
    for positon in range(word_len):
        if chosen_word[positon] == guess:
            display[positon] = guess

    # for incorrect word reduce lives and display lives left
    if not guess in chosen_word:
        user_lives -= 1
        print(f"Incorrect word, You have {user_lives} lives left")

        # No more life? End game, display game lost
        if user_lives == 0:
            game_over = True
            print("Game! Over, YOU LOSE!!!💀💀💀")
            break

    else:
         print(display)
        
    guess = input("Guess a letter: ").lower()



    





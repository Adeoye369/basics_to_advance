
from random import randint

EASY_LEVEL_LIFE = 10
HARD_LEVEL_LIFE = 5

def check_answer(guess, answer, turns):
    """check answer angainst guess, return the 'turns' """
    if guess > answer:
        print("Too high")
        return turns - 1

    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}")
        return turns


def set_difficulty():
    level = input("Choose a difficulty, Type 'easy' or 'hard'")
    if level == 'easy':
        return EASY_LEVEL_LIFE
    else:
        return HARD_LEVEL_LIFE

    

def guess_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    # let computer guess
    computer_ans = randint(1, 100)
    # print(f"DEV::the correct answer is {computer_ans}")

    turns = set_difficulty()

    # repeat the guessing functionality 
    user_guess = 0
    while user_guess != computer_ans:
        # Notify the number of life left
        print(f"You have {turns} turns left")

        #Let the user guess a number
        user_guess = int(input("What is the number: "))

        # Check if the number guessed is correct
        turns = check_answer(turns=turns, guess=user_guess, answer=computer_ans)

        if turns == 0:
            print("You run out of guesses, Your Loss")
            return
        elif user_guess != computer_ans:
            print("Guess again!\n")

guess_game()
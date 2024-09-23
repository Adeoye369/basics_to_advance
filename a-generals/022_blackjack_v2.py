import random
import os 
from art import blackjack_logo

# cards
def deal_card():
    """Deal random cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and returns the score cal. from cards """
    if sum(cards) == 21 and len(cards) == 2:
        return 0 # score of blackjack
    
    # Ace card use case
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_sc, computer_sc):
    if user_sc == computer_sc:
        return "Draw Scores"
    elif computer_sc == 0:
        return "You Lose, opponent has blackjack"
    elif user_sc == 0:
        return "You Win with a blackjack"
    elif user_sc > 21:
        return "You went over, you lose"
    elif computer_sc > 21:
        return "Opponent went over, You win"
    elif user_sc > computer_sc:
        return "You win"
    else:
        return "You lose"



def play_game():

    print(blackjack_logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # for the users
    while not is_game_over:
        # if the user or computer has blackjack(0) or if the score is over 21, game ends
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"  Your cards: {user_cards}, current score: {user_score}")
        print(f"  Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True 
        else:
            user_should_deal = input(" Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    # case of computer card deal
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # print game details
    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    # compare the computer and user score
    print(compare(user_sc=user_score, computer_sc=computer_score))

play_game()

while input("Do you want to keep playing the game? y/n:") == 'y':
    os.system('cls')
    play_game()

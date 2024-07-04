
import random

game_over = False

# random selection
def deal_card():
    return random.randint(1, 11)


computer = {"cards": [], "score": 0}
player = {"cards": [], "score": 0}

print("Wellcome to BlackJack!!\n\n")

player["cards"].extend([deal_card(), deal_card()])
computer["cards"].extend([deal_card(), deal_card()])

print(f"The first computer card is {computer['cards'][0]}")
print(f"Yor player deals are: {player['cards']}")


while not game_over:

    is_game_end = input("Type 'y' to get another card 'n' to pass:").lower()
    
    if is_game_end == 'y':
        player["cards"].append(deal_card())

        print(f"Yor player deals are: {player['cards']}")

        # Calculate player score
        for card in player["cards"]:
            player["score"] += card
        
        print(f"my score: {player['score']}")

        if player["score"] > 21:
            game_over = True
            print(f"You Lose! score is {player['score']} and is greater than 21")
            break

    elif is_game_end == 'n':
        game_over = True

        # Calculate computer score
        for card in computer["cards"]:
            computer["score"] += card

        # Calculate player score
        for card in player["cards"]:
            player["score"] += card


print(f"Computer scores is {computer['score']} and your score is {player['score']}")
 
if computer["score"] > player["score"]: 
    print(f"You Lose!😞. Computer wins")

elif computer["score"] < player["score"]:
    print("Player wins!!!🎉🎉🎉")

from game_data import hl_data
import random


# fetch ig data at random
def gen_random_account():
    """Generate two ig account at random, returns the data"""
    return random.choice(hl_data)


# function to check whose data is greater
def check_user_guess(data1, data2, guess):
    """Check whose followers is greater and returns the greater data"""

    if guess == 'H' and data2["follower_count"] > data1["follower_count"]:
        print(f"Correct, {data2['name']}, followers: {data2['follower_count']} > {data1['name']}, followers: {data1['follower_count']}\n")
    
    elif guess == 'L' and data2["follower_count"] < data1["follower_count"]:
        print(f"Correct, {data2['name']}, followers: {data2['follower_count']} < {data1['name']}, followers: {data1['follower_count']}\n")
    
    elif guess == 'H' and data2["follower_count"] < data1["follower_count"]:
        print(f"Wrong, {data2['name']}, followers: {data2['follower_count']} < {data1['name']}, followers: {data1['follower_count']}\n")
        return
    
    elif guess == 'L' and data2["follower_count"] > data1["follower_count"]:
        print(f"Wrong, {data2['name']}, followers: {data2['follower_count']} > {data1['name']}, followers: {data1['follower_count']}\n")
        return
    
    return data2



user_score = 0
   
# data 1, data 2
acctA_data = gen_random_account()

while acctA_data != None:

    acctB_data = gen_random_account()

    # Case of same data, get new random acct.
    if acctA_data == acctB_data:
        acctB_data = gen_random_account()

    # Ask user which is greater data1 or data 2
    user_suggest = input(f"\nthe acct. A=>  {acctA_data['name']} has {acctA_data['follower_count']} Million follwers,\nand acct. B=> is {acctB_data['name']}, is B Higer or Lower(H\L): ").upper()

    acctA_data = check_user_guess(data1=acctA_data, data2=acctB_data, guess=user_suggest)
    if acctA_data == None:
        print("sorry! You Lose, Your score is ", user_score )
    else:
        user_score+= 1










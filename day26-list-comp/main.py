import pandas as pd

nato_data = pd.read_csv("./day26-list-comp/nato_alphabet.csv")

nato_dict = {row.letter: row.code for(index, row) in nato_data.iterrows() }

# get the user name input
user_name = input("Enter your name:").upper()

user_nato_name = [nato_dict[nato] for nato in user_name ]
print(user_nato_name)


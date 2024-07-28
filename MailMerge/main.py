#TODO: Create a letter using starting_letter.txt 
placeholder = "[name]" # Names to be replaced

with open("./MailMerge/Input/Names/invited_names.txt", mode='r') as file:
    name_list = [f.strip() for f in file.readlines()]

# open the "example.txt"
with open("./MailMerge/Input/Letters/starting_letter.txt", mode='r') as letter_content:
    template_letter = letter_content.read()

for name in name_list: 
    # replace name in temp letter
    new_letter = template_letter.replace(placeholder, name)
    # write a new letter 
    with open(f"./MailMerge/Output/ReadyToSend/invited_for_{name}.txt", mode='w') as completed_letter:
        completed_letter.write(new_letter)


    

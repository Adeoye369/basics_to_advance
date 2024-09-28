import tkinter as tk
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
app_dir = "./day31-flashcard"
current_card= {}

# Load the Csv data
try:
    data = pd.read_csv(f"{app_dir}/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(f"{app_dir}/data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    win.after_cancel(flip_timer) # remove timer if next
    current_card = random.choice(to_learn)

    # flip to the front card
    canvas.itemconfig(card_title, text="French", fill="#ff00aa")
    canvas.itemconfig(card_word, text=current_card["French"], fill="#aa00ff")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = win.after(3000, flip_card) # recreate the timer


def flip_card():
    # flip the the backcard
    canvas.itemconfig(card_title, text="English", fill = "#333")
    canvas.itemconfig(card_word, text=current_card["English"], fill="#fff")
    canvas.itemconfig(card_bg, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(f"{app_dir}/data/words_to_learn.csv", index=False)
    next_card()

win = tk.Tk()
win.title("flash card")
win.config(bg=BACKGROUND_COLOR, padx=20, pady=20)
flip_timer = win.after(3000, func=flip_card)

# Load the Images data
wrong_img = tk.PhotoImage(file=f"{app_dir}/images/wrong.png")
right_img = tk.PhotoImage(file=f"{app_dir}/images/right.png")
card_front_img = tk.PhotoImage(file=f"{app_dir}/images/card_front.png")
card_back_img = tk.PhotoImage(file=f"{app_dir}/images/card_back.png")

# Flash cards widgets
cvs_width = 800
cvs_height = 530 
canvas = tk.Canvas(win, width=cvs_width, height=cvs_height, highlightthickness=0, background=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# Front Image BG
card_bg = canvas.create_image(cvs_width/2, cvs_height/2, image=card_front_img)
# Title Text
card_title = canvas.create_text(400, 150, text="French", fill="#ff00aa", font=("Ariel", 30, "italic") )
# Word text
card_word = canvas.create_text(400, 235, text="Voudrais", fill="#aa00ff", font=("Ariel", 60, "bold"))


# Button widgets
unknown_btn = tk.Button(win, image=wrong_img, highlightthickness=0, border=0, command=next_card)
known_button = tk.Button(win, image=right_img, highlightthickness=0, border=0, command=is_known)
unknown_btn.grid(row=1, column=0)
known_button.grid(row=1, column=1)

next_card()

win.mainloop()



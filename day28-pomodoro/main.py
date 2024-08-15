
import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2 #25
SHORT_BREAK_MIN = 0.05 #5
LONG_BREAK_MIN = 0.1 #20
BUTTON_FONT = ("Consolas", 15, "bold") 
is_countdown = False
is_count_finished = False
g_c = 0
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checks_label.config(text="")

    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def play_pause():
    global is_countdown

    if not is_count_finished: # not done
        is_countdown = not is_countdown # flip count

        # continue countdown
        if g_c > 0 and is_countdown:
            pause_btn.config(text="Pause")
            count_down(g_c, 0)
        else:
            pause_btn.config(text="Play")

def start_timer():
    global is_count_finished
    global is_countdown
    global g_c
    global reps
    # start all over again
    is_count_finished = False
    is_countdown = True
    g_c = 0

    reps+=1
    
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    
    if reps %8 == 0:
        count_down(long_break_sec, 0)
        title_label.config(text="Long Break", fg=GREEN)
    elif reps %2 == 0:
        count_down(short_break_sec, 0)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec, 0)
        title_label.config(text="Work Time", fg=RED)

    print("Starting count_down")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count, g_count):
    global is_count_finished
    global is_countdown
    global g_c
    global timer

    # end count once '0'
    if count == 0 : 
        is_count_finished = True
        g_c = 0
        print("==Finished Count==")
    if is_countdown:
        g_count = count # global count
        count_min = math.floor(count/60)
        count_sec = count % 60

        canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
        if count > 0:
            timer = root.after(1000, count_down, count - 1, g_count)
        else:
            start_timer()
            marks =""
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                marks += "✔️"
            checks_label.config(text=marks)
    else:
        g_c = g_count # update global count
        print(g_count)

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Pomodoro")
root.config(padx=50, pady=50, bg=YELLOW)


# Timer Stage label
title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"), pady=20)
title_label.grid(row=0, column=1)

# Create the canvas 
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# loading image
tomato_img = tk.PhotoImage(file="day28-pomodoro/tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold" ))
canvas.grid(row=1, column=1)

# count_down(5)

# Start Button
start_btn = tk.Button(text="Start", font=BUTTON_FONT, command=start_timer)
start_btn.grid(row=2, column=0)

# pause button
pause_btn = tk.Button(text=f"Pause", font=BUTTON_FONT, command=play_pause)
pause_btn.grid(row=3, column=0)

# Reset Button
reset_btn = tk.Button(text="Reset", font=BUTTON_FONT, command=reset_timer)
reset_btn.grid(row=2, column=2)

# Check mark Label
checks_label= tk.Label(fg=GREEN, bg=YELLOW, font=("Arial", 8))
checks_label.grid(row=3, column=1)


root.mainloop()

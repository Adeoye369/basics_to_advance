import tkinter as tk

BG_COLOR = "#222"
FG_COLOR = "#eee"


# btn1
def btn1_enter_cmd():
    label1.config(text=input1.get())
    print("ME CLICKED!")


window_tk = tk.Tk()

# create window basic
window_tk.title("Test Program")
window_tk.minsize(width=300, height=300)
window_tk.config(bg=BG_COLOR)


# Label example
label1 = tk.Label(text="User name:", font=("Cursive", 10, "italic"))
label1.config(bg=f"{BG_COLOR}444", fg=FG_COLOR)
label1.pack()

# Entry
input1 = tk.Entry()
input1.pack()

# Button 1
btn1 = tk.Button(text="Enter", bg=f"{BG_COLOR}555", fg="white", command=btn1_enter_cmd)
btn1.pack()

window_tk.mainloop()




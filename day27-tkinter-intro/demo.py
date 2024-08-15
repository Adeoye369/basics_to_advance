import tkinter as tk

BG_COLOR = "#222"
FG_COLOR = "#eee"


win = tk.Tk()
win.title("Basic demo")
win.minsize(width=500, height=500)
win.config(bg=BG_COLOR)

def entry_textout(): print(entry.get())
# Entries==============================#
entry = tk.Entry(width=30)

# Add some text to begin with
entry.insert(tk.END, string="Some text begin with")
# print(entry.get()) # Get text in entry
entry.grid(column=0, row=0)

# Button===============================#
def action(): print("Btn: Just do it!")
btn = tk.Button(text="Click it!", command=entry_textout)
btn.grid(column=1, row=0)

# Text Widget =========================#
text = tk.Text(height=10, width=30)
text.focus() # Puts cursor in textbox
text.insert(tk.END, "Example of multi-line.") # Text to begin with

# '1.0' means get line "1" from "0" character
print()
text.grid(rowspan=2, pady=20, padx= 20)

# Get the Text Content
def text_action(): 
    text_val = text.get("1.0", tk.END)
    label1.config(text=text_val)

btn1 = tk.Button(text="Get Text Content", command=text_action)
btn1.grid()
label1 = tk.Label(text="", fg=FG_COLOR, bg=BG_COLOR)
label1.grid()

# SpinBox ===================>
def spinbox_action(): print(spinbox.get())

spinbox = tk.Spinbox(from_=1, to=6, width=5, command=spinbox_action)
spinbox.grid()


# Scale =====================>
def scale_action(val):
    print(v1.get())

v1 = tk.IntVar()
scale = tk.Scale(from_=0, to=100, variable=v1, command=scale_action)
scale.grid()

# CheckBox ==================>
def checkbtn_action():
    # print '1' - ON,  '0' - OFF
    print(checked_state.get())

# variable to hold check
checked_state = tk.IntVar()

checkbutton = tk.Checkbutton(text="Turn off Nude", variable=checked_state, command=checkbtn_action)
checkbutton.grid()


# Radio Button ==============>
def radio_action():
    print(radio_state.get())

# variable to hold which value is checked
radio_state = tk.IntVar()

radiobtn1 = tk.Radiobutton(text="30 sec", value=30, variable=radio_state, command=radio_action)
radiobtn2 = tk.Radiobutton(text="60 sec", value=60, variable=radio_state, command=radio_action)
radiobtn3 = tk.Radiobutton(text="2 mins", value=99, variable=radio_state, command=radio_action)
radiobtn1.grid()
radiobtn2.grid()
radiobtn3.grid()


# List Box ================>
def listbox_action(event):
    # Get current selection from listbox
    print(listbox.get(listbox.curselection()))

fruits = ["Apple", "Pear", "Orange", "Banana"]

listbox = tk.Listbox(height=4)
for i in range(len(fruits)): listbox.insert(i, fruits[i])

listbox.bind("<<ListboxSelect>>", listbox_action) # Attach to the function
listbox.grid()

win.mainloop()
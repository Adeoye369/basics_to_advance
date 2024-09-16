import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()
win.minsize(300, 500)
win.title("Keyboard evernt Bind Test")
win.config(padx=20)

fram1 = ttk.LabelFrame(win, text="Keyboard Bind", padding="20 20")
fram1.pack()

label1 = ttk.Label(fram1, text= "Event Goes", background="#ffffee", padding=(20, 10))
label1.pack(fill=tk.X)


# General key bind
win.bind("<Key>", lambda e : label1.config(text=f"{e.char}, {e.keysym}, {e.keycode}"))

# Using lambda expression to bind key event
win.bind("a", lambda e : label1.config(text="key small 'a' is pressed"))
win.bind("A", lambda e : label1.config(text="key Capital 'A' is pressed")) # Note its case sensitive
# key sequence example
win.bind("aZ", lambda e : label1.config(text="aZ in is pressed")) # only when the other is fulfilled

# Special keys binding
# <Return>, <Up>, <Right> <Down> - arrows
# <space>, <less>
count = 0
def add_count(num) : 
    global count
    count += num
    return count

win.bind("<Up> ", lambda e : print(e.keysym, add_count(1)) )
win.bind("<Down> ", lambda e : print(e.keysym, add_count(-1)) )

# Combined special keys bind with 
win.bind("<Control-Up>", lambda e : print(e.keysym, "Control-up"))
win.bind("<Alt-m>", lambda e : print(e.keysym, "Alt m pressed key"))
win.mainloop()
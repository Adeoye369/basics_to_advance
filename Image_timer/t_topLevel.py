import tkinter as tk

def activate_toplevel1():
    top1 = tk.Toplevel()
    top1.minsize(150, 150)
    top1.title("I AM TOP-LEVEL 1")

    label_top1 = tk.LabelFrame(top1, text="Top 1 Label", padx=10, pady=10)
    tk.Button(label_top1, text="CLiCK ME", command=open_topLevel2).pack()
    tk.Button(label_top1, text="Exit", fg="red", command=top1.destroy).pack()

    label_top1.pack()

    top1.mainloop()


def open_topLevel2():
    tp2 = tk.Toplevel()
    tp2.geometry("250x400")
    tp2.title("Top 2")

    tk.Label(tp2, text="this is my label").pack()
    tk.Button(tp2, text="Exit", fg="red", command=tp2.destroy).pack()
    tk.Button(tp2, text="Exit Main", fg="red", command=win.destroy).pack()

    tp2.mainloop()


win  = tk.Tk()
win.minsize(250, 250)
win.title("Top level test")

tk.Label(win, text="This is the Main window" ).pack()
tk.Button(text="Start", command=activate_toplevel1).pack()




win.mainloop()
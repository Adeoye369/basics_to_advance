import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Testing Scrollabe Frame")
win.minsize(300, 300)
win.config(padx=20, pady=20)

s = ttk.Style()
s.configure('my.TLabelframe', borderwidth=20, relief='solid', labelmargins=20, background="#ff99aa")
s.configure('my.TLabelframe.Label', font=('Helvetica', 10, 'italic'))

# contianer to hold canvas
container = ttk.LabelFrame(win, text="Container Frame", width=400, height=200, style="my.TLabelframe", padding=(20, 20))

canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)

s.configure("my2.TLabelframe", background="green")
scrollable_frame = ttk.Frame(canvas, style="my2.TLabelframe")

scrollable_frame.bind(
        "<Configure>", 
        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)


# Load widget into the container
for i in range(50):
    row_count = i // 4
    col_count =  i % 4
    ttk.Button(scrollable_frame, text=f"Some Button ", padding=(20, 10)).grid(row=row_count, column=col_count, sticky=tk.N)

container.pack()
canvas.pack(side="left", fill="both", expand=True, ipadx= 20, ipady = 20)
scrollbar.pack(side="right", fill="y")

win.mainloop()
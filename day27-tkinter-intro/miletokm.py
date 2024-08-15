import tkinter as tk

win = tk.Tk()
win.title("Mile to Km Converter")
win.config(padx=10, pady=10)

l_frame = tk.Frame(win)
l_frame.grid(column=1, row=0)

r_frame = tk.Frame(win)
r_frame.grid(column=0, row=1)

miles_label = tk.Label(l_frame, text="Miles")
miles_entry = tk.Entry(l_frame)
miles_label.grid(column=0, row=1)
miles_entry.grid(column=1, row=1)

km_label = tk.Label(r_frame, text="Km")
km_entry = tk.Entry(r_frame)
km_label.grid(column=0, row=1)
km_entry.grid(column=1, row=1)


win.mainloop()

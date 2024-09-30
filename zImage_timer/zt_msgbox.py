import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk

win = tk.Tk()

win.minsize(300, 300)
win.title("testing msg Box")

def showmsg(type):
    output = None

    if type == "AYNC":
        output = msgbox.askyesnocancel(title = "Example0", message="Do you know what to do? ", parent=win)

    elif type == "AYN":
        output = msgbox.askyesno(title= "Exampe1", message="Do you know me?")

    elif type == "AQ":
        output = msgbox.askquestion(title="about you", message="tell me about you")
    
    elif type == "SI":
        output = msgbox.showinfo("showinfo example", "this is a message box")

    print(f"Message {type} output is : {output}" )


btn1 = ttk.Button(win, text= "Press me!! AYNC " , padding="10 10", command= lambda : showmsg("AYNC"))
btn2 = ttk.Button(win, text= "Press me!! AYN " , padding="10 10", command= lambda : showmsg("AYN"))
btn3 = ttk.Button(win, text= "Press me!! AYQ " , padding="10 10", command= lambda : showmsg("AQ"))
btn4 = ttk.Button(win, text= "Press me!! SI " , padding="10 10", command= lambda : showmsg("SI"))
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()



win.mainloop()
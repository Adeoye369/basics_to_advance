import os
import tkinter as tk
import tkinter.filedialog as fd

from utility import load_image
from timer_window import TimerWindow
from image_viewer import ImageViewer


class Draw_App():

    def __init__(self) -> None:

        #### ==== ATTRIBUTES ==== ####
        self.img_btn_list = [] # Container to hold the images
        self.canvas = None

        # Create the basic 
        self.win = tk.Tk()
        self.win.title("Image Timer")
        self.win.minsize(200, 200)
        self.win.config(padx=20, pady=20)

        self.display_UI()

        # main loop
        self.win.mainloop()

    def openfile(self):

        new_img_files = fd.askopenfilenames(parent=self.win, title="Choose a File")
        print(self.win.splitlist(new_img_files))

        self.display_images(new_img_files)

    def display_UI(self):
        
        # Select image Frame
        self.select_frame = tk.LabelFrame(self.win, text="select Images", padx=10, pady=10,)
        self.select_frame.pack()

        self.file_btn =  tk.Button(self.select_frame, text="select Image files",  command=self.openfile)
        self.file_btn.grid(row=1, column=1)

        # Display list Frame
        self.images_frame = tk.LabelFrame(self.win, text="image list", padx=10, pady=10,)
        self.images_frame.pack()

        # Button to display image display from begining
        self.start_btn = tk.Button(text="START" )
        self.start_btn.pack_forget()

    def display_images(self,img_files):

        # Reset the list if not empty
        self.img_btn_list.clear()

        index = 0
        row = 0; col = 0

        for img in img_files:
            print(img)
            row = index//4
            col =  index%3

            new_img = ImageViewer()
            new_img.process_image(img)
            new_img.display_button(self.images_frame, row, col)
            # Add image to list
            self.img_btn_list.append(new_img)
            index+=1

        self.start_btn.pack()
        self.start_btn.config(command=self.start_timer_window)

    def start_timer_window(self):

        t = TimerWindow(self.img_btn_list)
        t.loop()

if __name__ == "__main__":
    Draw_App()
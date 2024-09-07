import os
import tkinter as tk
import tkinter.filedialog as fd

from PIL import ImageTk
from functools import partial

from utility import load_image


class Draw_App():

    def __init__(self) -> None:

        #### ==== ATTRIBUTES ==== ####
        self.img_btn_list = {} # Container to hold the images
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

    def view_image(self, image, filename):

        self.top1 = tk.Toplevel()
        self.top1.minsize(300, 300)
        self.top1.title("Image view")

        label1 = tk.Label(self.top1, text=f"Image:{filename}")
        label1.pack()

        canvas_width = image.width()
        canvas_height = image.height() 
        self.canvas = tk.Canvas(self.top1)
        self.canvas.pack(padx=10, pady=10)
        self.canvas.create_image(canvas_width/2, canvas_height/2, image=image)

        self.top1.mainloop()


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
        self.start_btn = tk.Button(text="START", command=self.view_image )
        self.start_btn.pack_forget()


    def display_images(self,img_files):

        # Reset the image list
        if self.img_btn_list != {}: 
            for img, img_btn in self.img_btn_list.items():
                del img
                img_btn.destroy()

        index = 0
        row = 0; col = 0
        for img in img_files:
            print(img)
            row = index//4
            col =  index%3
            cropped_image = ImageTk.PhotoImage(load_image(img, 70))
            full_image =ImageTk.PhotoImage(load_image(img))
            name = os.path.splitext(os.path.basename(img))[0] # get the name

            img_btn = tk.Button(self.images_frame, image=cropped_image, compound=tk.LEFT, 
                                text= f"{name[:6]}..." if len(name)> 6 else name,
                                 command=partial(self.view_image, full_image, name) )
            
            img_btn.grid(row=row ,column=col)
            self.img_btn_list.setdefault(cropped_image, img_btn)
            index+=1

        self.start_btn.pack()

if __name__ == "__main__":
    Draw_App()
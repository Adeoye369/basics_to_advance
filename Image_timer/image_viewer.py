from PIL import ImageTk
from utility import load_image
from functools import partial
import os

from tkinter import ttk, Label, Canvas, Toplevel, TOP


class ImageViewer():
    
    def __init__(self, image_name="", thumbnail_image=None, full_image=None, 
                 image_button=None):
        
        self._name = image_name
        self._thumb_img = thumbnail_image
        self._full_img = full_image
        self._img_btn = image_button

    @property 
    def name(self):return self._name
    @name.setter
    def name(self, val): self._name = val
    
    @property
    def full_img(self): return self._full_img
    @full_img.setter
    def full_img(self, val): self._full_img = val

    
    @property
    def thumb_img(self): return self._thumb_img
    @thumb_img.setter
    def thumb_img(self, val): self._thumb_img = val
    
    @property # image tkinter Button
    def img_btn(self): return self._img_btn
    @img_btn.setter
    def img_btn(self, val): self._img_btn = val

    def process_image(self, image_path):
        ''' Convert image path to tk image thumb and full image'''
        thumb_size = 80
        self._name = os.path.splitext(os.path.basename(image_path))[0] # get the name
        self._thumb_img = ImageTk.PhotoImage(load_image(image_path, thumb_size))
        self._full_img =ImageTk.PhotoImage(load_image(image_path))

    def display_button(self, root, row, col):
        ''' Display the Button of the image'''
        self._img_btn = ttk.Button(root, image=self._thumb_img, compound=TOP, 
                                text= f"{self._name[:10]}..." if len(self._name)> 10 else self._name,
                                 command=self.view_image)
            
        self._img_btn.grid(row=row ,column=col)

    def view_image(self):
        ''' view the tk_image  and the filename'''
        self.top1 = Toplevel()
        self.top1.minsize(300, 300)
        self.top1.title("Image view")

        label1 = Label(self.top1, text=f"Image:{self.name}")
        label1.pack()

        self.canvas = self.render_full_image( self.top1)
        self.canvas.pack()

        self.top1.mainloop()

    def render_full_image(self, root) -> Canvas :
        ''' Draws the full image size on the canvas
            NB: Remember to set .pack() or .grid(...) on the return canvas
        '''
        w = self.full_img.width() +10
        h = self.full_img.height() +10 

        cvs = Canvas(root, width=w, height=h)
        cvs.create_image(w/2, h/2, image=self.full_img)
        return cvs

    @staticmethod
    def render_image(root, tk_img, w, h):
        ''' draws the canvas for the tk image to fit the size
            NB: Remember to set .pack() or .grid(...) on the return canvas
        '''
        canvas = Canvas(root, width=w, height=h)
        canvas.create_image(w/2, h/2, image=tk_img)
        return canvas
    
    def delete_image(self):
        self._img_btn.destroy()

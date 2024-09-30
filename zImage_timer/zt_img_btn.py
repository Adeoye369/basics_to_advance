import tkinter as tk
import tkinter.filedialog as fd
from PIL import ImageTk, Image
import glob, os


def load_image(filepath, new_width = None, new_height= None, reduce_by=1) :
    '''
    This loads image using Image class from the PIL Library

    Parameters: 
    filepath (string) : path to the image file
    new_width (int) : Specify new resize width, None if not specified
    new_height (int) : specify new resize height, None if not specified
    reduce_by(float) : proportional resizing by value specified

    Returns:
    Image : PIL class for Images '''
    
    import math
    img = Image.open(filepath)

    if new_width and new_height:
        img = img.resize((new_width, new_height))

    elif new_width and not new_height:
        aspect_ratio = img.size[1]/img.size[0]
        img = img.resize((new_width, math.floor(new_width*aspect_ratio)))
    
    elif new_height and not new_width:
        aspect_ratio = img.size[0] /img.size[1]
        img = img.resize((math.floor(new_height*aspect_ratio), new_height))
    
    elif reduce_by < 1:
        img = img.resize((math.floor(img.size[0]*reduce_by), math.floor(img.size[1]*reduce_by)))

    return img


def openfile():
    new_img_files = fd.askopenfilenames(parent=win, title="Choose a File")
    print(win.splitlist(new_img_files))

    display_images(new_img_files)


img_btn_list = {} # Container to hold the images

def display_images(img_files):
    index = 0
    # for img in glob.glob("image_timer\imgs\*.png"):
    for img in img_files:
        print(img)
        row = index//4
        col =  index%3
        img1 = ImageTk.PhotoImage(load_image(img, 70))
        
        name = os.path.splitext(os.path.basename(img))[0] # get the name

        img_btn = tk.Button(images_frame, image=img1, compound=tk.LEFT, text= f"{name[:6]}..." if len(name)> 6 else name )
        img_btn.grid(row=row ,column=col)
        img_btn_list.setdefault(img1, img_btn)
        index+=1

win = tk.Tk()
win.minsize(400, 400)
win.title("Img Btn text")

select_frame = tk.LabelFrame(win, text="select Images", padx=10, pady=10,)
select_frame.pack()
images_frame = tk.LabelFrame(win, text="image list", padx=10, pady=10,)
images_frame.pack()

file_btn =  tk.Button(select_frame, text="select Image files",  command=openfile)
file_btn.grid(row=1, column=1)


win.mainloop()
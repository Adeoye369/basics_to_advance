import tkinter.filedialog as fd
from PIL import Image

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


def min_sec(count):
    return count // 60, count % 60

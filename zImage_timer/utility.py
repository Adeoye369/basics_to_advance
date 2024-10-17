
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
    Image : PIL class for Images 
    '''
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

    elif img.size[0] > 960 :
        aspect_ratio = img.size[1] / img.size[0]
        img = img.resize((960, math.floor(960 * aspect_ratio)))
    
    return img


def min_sec(count):
    return count // 60, count % 60



class WidgetUtil():
    
       
       @classmethod
       def get_and_validate_drawtime(cls, entryWidget, warningWidget):
        '''
        Check if the draw time is valid value or through 
        Valuerror warning if failed
        @return int value
        '''
        default_entry = 30
        try:
            entry_value = entryWidget.get()

            if(entry_value == ""): 
                if warningWidget: warningWidget.config(text = "Time is empty, will use default")
                return default_entry
             
            entry_value = int(float(entry_value))

            if(entry_value == 0): 
                if warningWidget: warningWidget.config(text = "Zero value, will use default")
                return default_entry

        except ValueError:
            if warningWidget: warningWidget.config(text = "Invalid Input, will use default")
            return default_entry

        # All is good, Reset the warning label,
        if warningWidget: warningWidget.config(text = "")

        return entry_value 


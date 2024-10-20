import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd

from utility import load_image, WidgetUtil
from timer_window import TimerWindow
from image_viewer import ImageViewer
from scrollable_frame import ScrollableFrame
import time

class Draw_App():

    def __init__(self) -> None:

        #### ==== ATTRIBUTES ==== ####
        self.img_btn_list = [] # Container to hold the images
        self.time_duration = 0
        self.canvas = None


        # Create the basic 
        self.win = tk.Tk()
        self.win.title("Image Timer")
        self.win.minsize(400, 300)
        self.win.config(padx=20, pady=20)

        # value for grid division
        self.image_grid_div = 4

        #Get the current screen width and height
        self.screen_size = self.win.winfo_screenwidth(), self.win.winfo_screenheight()

        self.display_UI()

        # main loop
        self.win.mainloop()

    def openfile(self):

        self.new_img_files = fd.askopenfilenames(parent=self.win, title="Choose a File")
        # print(self.win.splitlist(new_img_files))

        if self.new_img_files:
            self.display_images()

    def display_UI(self):
        
        # Select image Frame
        self.select_frame = ttk.LabelFrame(self.win, text="", padding=(30, 30))
        self.select_frame.pack(fill=tk.BOTH, expand=True)

                # Display list Frame
        self.images_frame = ScrollableFrame(self.win, padding=(10,10))
        self.images_frame.pack_forget()

        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 20, 'bold'))
        self.file_btn =  ttk.Button(self.select_frame, text="select Image files",  style='my.TButton', command=self.openfile, padding=(10, 20))
        self.file_btn.pack(fill=tk.BOTH, ipady=30)


        # Set Timer option list Frame
        self.set_time_frame = ttk.LabelFrame(self.win, text="Select Duration", padding=(10, 10))
        self.set_time_frame.pack(fill=tk.BOTH)

        
        # Button to display image display from begining
        self.start_btn = ttk.Button(text="START", padding=(10, 10) )
        self.start_btn.pack_forget()


    def resize_scrollable_frame(self, e):
        time.sleep(0.05)
        self.image_grid_div = e.width // 100

        self.render_button_into_frame()


    def render_button_into_frame(self):
       
        # Reset the list if not empty
        if self.img_btn_list: 
            for img in self.img_btn_list: img.delete_image() # delete button in memory
            self.img_btn_list.clear() # empty the list

       
        index = 0
        row_count = 0; col_count = 0

        for img in self.new_img_files:
            row_count = index // self.image_grid_div
            col_count =  index % self.image_grid_div


            new_img = ImageViewer(screen_size=self.screen_size, image_path=img)
            new_img.process_image()
            new_img.display_button(self.images_frame, row_count, col_count)
            # Add image to list
            self.img_btn_list.append(new_img)
            index+=1


    def display_images(self):

        self.images_frame.pack(fill=tk.BOTH)
        self.images_frame.bind("<Configure>", self.resize_scrollable_frame)
        
        self.render_button_into_frame()


        # display duration options
        self.display_duration_options_UI()

        self.start_btn.pack()
        self.start_btn.config(command=self.start_timer_window)



    def display_duration_options_UI(self):
        ''' Display time duration options User Interface '''
        # Radio Button to display time select
        # Radio Button ==============>

        def radio_action():
            # print(radio_value.get())
            self.drawtime_entry.delete(0, tk.END)
            self.drawtime_entry.insert(tk.END,radio_value.get())
            self.time_duration = radio_value.get()

        # variable to hold which value is checked
        radio_value = tk.IntVar()

        self.radiobtn1 = ttk.Radiobutton(self.set_time_frame, text="30 sec", value=30, variable=radio_value, command=radio_action)
        self.radiobtn2 = ttk.Radiobutton(self.set_time_frame, text="60 sec", value=60, variable=radio_value, command=radio_action)
        self.radiobtn3 = ttk.Radiobutton(self.set_time_frame, text="2 mins", value=60*2, variable=radio_value, command=radio_action)
        self.radiobtn4 = ttk.Radiobutton(self.set_time_frame, text="3 mins", value=60*3, variable=radio_value, command=radio_action)
        self.radiobtn5 = ttk.Radiobutton(self.set_time_frame, text="5 mins", value=60*5, variable=radio_value, command=radio_action)
        self.radiobtn6 = ttk.Radiobutton(self.set_time_frame, text="10 mins", value=60*10, variable=radio_value, command=radio_action)
        
        self.radiobtn1.grid(row=0, column=0)
        self.radiobtn2.grid(row=0, column=1)
        self.radiobtn3.grid(row=0, column=2)
        self.radiobtn4.grid(row=0, column=3)
        self.radiobtn5.grid(row=0, column=4)
        self.radiobtn6.grid(row=0, column=5)

        # Display the time for the drawing interval
        self.drawtime_label = ttk.Label(self.set_time_frame, text="Time(sec)")

        self.drawtime_entry = ttk.Entry(self.set_time_frame, width=10)
        self.drawtime_entry.insert(tk.END, string="5")
        self.drawtime_label.grid(row=2, column=2)
        self.drawtime_entry.grid(row=2, column=3)



    def start_timer_window(self):
        self.time_duration = WidgetUtil.get_and_validate_drawtime(self.drawtime_entry, None)
        t = TimerWindow(self.img_btn_list, self.time_duration, self.screen_size)
        t.loop()

if __name__ == "__main__":
    Draw_App()
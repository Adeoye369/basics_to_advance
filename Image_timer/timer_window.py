import tkinter as tk
from utility import min_sec

class TimerWindow():

    def __init__(self, image_viewer_list):
        ''' Takes the list of ImageView generated '''

        # stores the ImageViewer list
        self.img_viewer_list = image_viewer_list

        # store slide index
        self.slide_idx = 0

                # help to know when to switch countdown display
        self.is_break = False 

        # when to skip the draw timer
        self.is_skip = False

        # keep track if countdown is active or not
        self.start_countdown = False
        self.is_count_finished = False

        self.reps = 0
        self.count_dwn = 0 # keep track of count for pause/play

        self.time_win = tk.Toplevel()
        self.time_win.minsize(300, 300)
        self.time_win.title("This the mim size")


        # print all image name and thumb tk
        for idx, img in enumerate( self.img_viewer_list ) :
            print(f"index: {idx}, {img.name}, {img.thumb_img}")

        self.displayUI()

        
    def displayUI(self):
        # UI for the labels
        self.settings_frame = tk.LabelFrame(self.time_win, text="settings", padx=10, pady=10)
        self.settings_frame.grid(row=0, column=0)

        self.img_list_frame = tk.LabelFrame(self.time_win, text="Image", padx=10, pady=10)
        self.img_list_frame.grid(row=0, column=1)

        self.btn0 = tk.Button(  self.settings_frame, text="Btn1")
        self.btn0.grid(row=0, column=0)


        # Display the image select in the 
        self.canvas = self.img_viewer_list[0].render_full_image(self.img_list_frame)
        self.canvas.grid(row=0, column=0, sticky=tk.NSEW)

        # Left Button
        self.left_btn = tk.Button(self.img_list_frame, text="Left", command=lambda:self.slide_dir(-1))
        self.left_btn.grid(row=0, column=0, sticky=tk.W)

        # Right Button
        self.right_btn = tk.Button(self.img_list_frame, text="Right", command=lambda:self.slide_dir(1))
        self.right_btn.grid(row=0, column=0, sticky=tk.E)

        # draw timer text on canvas
        cvs_width = self.img_viewer_list[0].full_img.width() # canvas width 
        self.timer_text = self.canvas.create_text(cvs_width-30, 30, text="00:00", fill="gray", font=("Courier", 20, "bold" ))
        
        self.start_timer()


    # === Slider Operator === #
    def slide_dir(self, count):

        self.slide_idx += count
        list_idx = len(self.img_viewer_list)-1

        # Reset slider index if at RIGHT extreme
        if (self.slide_idx > list_idx ): self.slide_idx = list_idx

        # Reset slider index if at LEFT extreme
        elif(self.slide_idx < 0) : self.slide_idx = 0
        
        # Display image slide
        self.canvas = self.img_viewer_list[self.slide_idx].render_full_image(self.img_list_frame)
        self.canvas.grid(row=0, column=0, sticky=tk.NSEW)

               # draw timer text on canvas
        cvs_width = self.img_viewer_list[0].full_img.width() # canvas width 
        self.timer_text = self.canvas.create_text(cvs_width-30, 30, text="00:00", fill="#000", font=("Courier", 20, "bold" ))
        


        # Put Left and right button on top of canvas
        self.left_btn.lift()
        self.right_btn.lift()

       

    # === Create Timer UI ==== #

    # === Start Timer === #
    def start_timer(self):

        # start first countdown
        self.start_countdown = True
        self.count_down()

    # === Count down === #
    def count_down(self):

        # get the value assigned to slider
        # self.short_break_sec = self.break_val.get()
        self.short_break_sec = 0
        # self.draw_time_sec = self.get_and_validate_drawtime()
        self.draw_time_sec = 10
        self.reps += 1

        # start again is slide has reach the end
        if self.slide_idx == len(self.img_viewer_list)-1 : self.slide_idx = 0
        # Next the image
        self.slide_dir(1)

        # switch between `initial time interval` and `break time interval`
        if self.reps %2 == 0 and self.short_break_sec != 0:
            self.is_break = True
            self.time_interval = self.short_break_sec
            self.update_timer(self.time_interval)

        else :
            self.is_break = False
            self.time_interval = self.draw_time_sec
            self.update_timer(self.time_interval)
        

    '''======= Count down timer ======= '''
    
    # === update count === #
    def update_timer(self, count_dwn):


        # check if to start countdown
        if self.start_countdown or self.is_break: 

            # update timer text
            self.min, self.sec = min_sec(count_dwn)


            if not self.is_break:
                # Update canvas text normal interval
                self.count_dwn = count_dwn
                self.canvas.itemconfig(self.timer_text, text=f"{self.min:02d}:{self.sec:02d}" )
                # self.pause_btn.config(state=tk.NORMAL)
                # self.reset_btn.config(state=tk.NORMAL)

                 
            else:    
                # break time countdown display
                self.canvas.itemconfig(self.timer_text, text=f"{self.sec}" )
                # # prohibit clicking of pause btn
                # self.pause_btn.config(state=tk.DISABLED)
                # self.reset_btn.config(state=tk.DISABLED)
                
            # Count only positive values,
            if count_dwn > 0:
                    self.timer = self.time_win.after(1000, self.update_timer, count_dwn - 1)
        
            else: # Count has finished restart count

                # start countdown again
                self.count_down()


    def loop(self):
        self.time_win.mainloop()

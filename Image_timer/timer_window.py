import tkinter as tk
from tkinter import ttk
from utility import min_sec,load_image, WidgetUtil
from PIL import ImageTk

class TimerWindow():

    def __init__(self, image_viewer_list, timer_duration):
        ''' Takes the list of ImageView generated '''

        # stores the ImageViewer list and duration
        self.img_viewer_list = image_viewer_list
        self.time_duration = timer_duration


        # store slide index
        self.slide_idx = 0

                # help to know when to switch countdown display
        self.is_break = False 

        # when to skip the draw timer
        self.is_skip = False

        # keep track if countdown is active or not
        self.is_start_countdown = False
        self.is_count_finished = False

        self.reps = 0
        self.count_dwn = 0 # keep track of count for pause/play

        self.canvas = None
        self.drawtime_entry = None
        self.timer = None
        self.timer_text = None
        self.min = 0
        self.sec = 0

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
        self.settings_frame.grid(row=0, column=0, sticky="NSEW")

        self.img_list_frame = tk.LabelFrame(self.time_win, text="Image", padx=10, pady=10)
        self.img_list_frame.grid(row=0, column=1, rowspan=2)



        self.create_menu_UI()

        # Display the image select in the 
        self.canvas = self.img_viewer_list[0].render_full_image(self.img_list_frame)
        self.canvas.grid(row=0, column=0, sticky=tk.NSEW)

        # Left Button
        self.left_btn_image = ImageTk.PhotoImage(load_image("./image_timer/assets/left_arrow.png", 50))
        self.left_btn = ttk.Button(self.img_list_frame, image=self.left_btn_image, command=lambda:self.skip_image(-1))
        self.left_btn.grid(row=0, column=0, sticky=tk.W)

        # Right Button
        self.right_btn_image = ImageTk.PhotoImage(load_image("./image_timer/assets/right_arrow.png", 50))
        self.right_btn = ttk.Button(self.img_list_frame, image=self.right_btn_image, command=lambda:self.skip_image(1))
        self.right_btn.grid(row=0, column=0, sticky=tk.E)

        # Start the countdown
        self.start_timer()
        self.slide_dir(0)

    



    def create_menu_UI(self):
        ### ================= MENU FRAME =================== ### 
        # Radio Button to display time select
        # Radio Button ==============>
        def radio_action():
            print(radio_value.get())
            self.drawtime_entry.delete(0, tk.END)
            self.drawtime_entry.insert(tk.END,radio_value.get())
            self.time_duration = radio_value.get()
        

        # variable to hold which value is checked
        radio_value = tk.IntVar()

        self.radiobtn1 = tk.Radiobutton(self.settings_frame, text="30 sec", value=30, variable=radio_value, command=radio_action)
        self.radiobtn2 = tk.Radiobutton(self.settings_frame, text="60 sec", value=60, variable=radio_value, command=radio_action)
        self.radiobtn3 = tk.Radiobutton(self.settings_frame, text="2 mins", value=60*2, variable=radio_value, command=radio_action)
        self.radiobtn4 = tk.Radiobutton(self.settings_frame, text="3 mins", value=60*3, variable=radio_value, command=radio_action)
        self.radiobtn5 = tk.Radiobutton(self.settings_frame, text="5 mins", value=60*5, variable=radio_value, command=radio_action)
        self.radiobtn6 = tk.Radiobutton(self.settings_frame, text="10 mins", value=60*10, variable=radio_value, command=radio_action)
        
        self.radiobtn1.grid(row=0, column=0)
        self.radiobtn2.grid(row=0, column=1)
        self.radiobtn3.grid(row=1, column=0)
        self.radiobtn4.grid(row=1, column=1)
        self.radiobtn5.grid(row=2, column=0)
        self.radiobtn6.grid(row=2, column=1)

        # Display the time for the drawing interval
        self.drawtime_label = tk.Label(self.settings_frame, text="Time(sec)")

        self.drawtime_entry = tk.Entry(self.settings_frame, width=8)
        print(f"passing in time_duration: {self.time_duration}" )
        self.drawtime_entry.insert(tk.END, string=f"{self.time_duration}")


        self.warning_label = tk.Label(self.settings_frame, text="", fg="red", font=("Arial", 10, "italic"))
        self.drawtime_label.grid(row=3, column=0)
        self.drawtime_entry.grid(row=3, column=1)
        self.warning_label.grid(row=4, column=0, columnspan=2)

        # break time between each drawing 
        self.break_val = tk.IntVar()
        self.break_slider = tk.Scale(self.settings_frame, from_=0, to=15,  variable=self.break_val, orient=tk.HORIZONTAL)
        self.break_slider.set(3) # set default break time
        self.break_label = tk.Label(self.settings_frame, text="breaks (sec)" )
        self.break_label.grid(row=5, column=0, columnspan=2)
        self.break_slider.grid(row=6, column=0, columnspan=2)

        ### ================ PLAYBACK - FRAME ===================== ###
        # playback Frame
        self.playback_frame = tk.LabelFrame(self.time_win)
        self.playback_frame.config(padx=10, pady=10)
        
        self.playback_frame.grid(row=1, column=0, sticky="NSEW")
        self.playback_frame.columnconfigure(0, weight=1)


        self.pause_btn = tk.Button(self.playback_frame, text="PAUSE", command=self.play_pause)
        self.pause_btn.grid(row=1, column=0, sticky="NSEW")
       


    # skip the image
    def skip_image(self, direction_idx):
        self.is_skip = True
        self.slide_dir(direction_idx)
        self.skip_countdown()
        self.is_skip = False

    # === Slider Operator === #
    def slide_dir(self, index_dir):
            
        self.slide_idx  = self.slide_idx + index_dir
        list_idx = len(self.img_viewer_list)-1

        # Reset slider index if at RIGHT extreme
        if (self.slide_idx > list_idx ): self.slide_idx = list_idx

        # Reset slider index if at LEFT extreme
        elif(self.slide_idx < 0) : self.slide_idx = 0

        print(f"Current Slide_idx: {self.slide_idx} ")
    
        self.canvas = self.img_viewer_list[self.slide_idx].render_full_image(self.img_list_frame)
        self.canvas.grid(row=0, column=0, sticky=tk.NSEW)

            # draw timer text on canvas
        self.img_width = self.img_viewer_list[self.slide_idx].full_img.width() # canvas width 
        self.img_height = self.img_viewer_list[self.slide_idx].full_img.height() # canvas height

        self.timer_text = self.canvas.create_text(self.img_width-30, 30, text=f"{self.min:02d}:{self.sec:02d}", fill="#f9f9f9", font=("Courier", 20, "bold" ))



        # Put Left and right button on top of canvas
        self.left_btn.lift()
        self.right_btn.lift()

    def draw_blank_canvas(self):
        # draw blank canvas
            # Creates a rectangle of 60 x 50 (width x height)
        pos_x = 0
        pos_y = 0
        self.canvas.create_rectangle(pos_x, pos_y, 
                                        self.img_width + pos_x + 10, # pos_x(10) + width(500)
                                        self.img_height + pos_y + 10, # pos_y(10) + height(400)
                                    outline = "white", fill = "gray",
                                    width = 2)
        self.timer_text = self.canvas.create_text(self.img_width-30, 30, text=f"{self.short_break_sec}", fill="#f9f9f9", font=("Courier", 20, "bold" ))
        self.canvas.create_text(self.img_width/2, self.img_height/2, text=f"Get ready for the \n NEXT DRAWING >>>",  fill="#f5f5f5", font=("Courier", 30, "bold" ))   


  

    # === Start Timer === #
    def start_timer(self):

        # start first countdown
        self.is_start_countdown = True
        self.count_down()

    # === Count down === #
    def count_down(self):

        # get the value assigned to slider
        self.short_break_sec = self.break_val.get()
        self.draw_time_sec = WidgetUtil.get_and_validate_drawtime(self.drawtime_entry, self.warning_label)
        self.reps += 1

        # switch between `initial time interval` and `break time interval`
        if self.reps %2 == 0 and self.short_break_sec > 0:
            self.is_break = True
            self.time_interval = self.short_break_sec
            self.update_timer(self.time_interval)
            self.draw_blank_canvas()


        else :
            self.is_break = False

            # draw timer text on canvas
            self.min, self.sec = min_sec(self.draw_time_sec )

            self.time_interval = self.draw_time_sec
            self.update_timer(self.time_interval)

            # Next the image
            if self.reps > 1 and not self.is_skip : 
                self.slide_dir(1)

            

    '''======= Count down timer ======= '''
    
    # === update count === #
    def update_timer(self, count_dwn):


        # check if to start countdown
        if self.is_start_countdown or self.is_break: 

            # update timer text
            self.min, self.sec = min_sec(count_dwn)


            if not self.is_break:
                # Update canvas text normal interval
                self.count_dwn = count_dwn
                self.canvas.itemconfig(self.timer_text, text=f"{self.min:02d}:{self.sec:02d}")
                self.pause_btn.config(state=tk.NORMAL)
                # self.left_btn.config(state=tk.NORMAL)
                self.right_btn.config(state=tk.NORMAL)

                 
            else:    
                # break time countdown display
                self.canvas.itemconfig(self.timer_text, text=f"{self.sec}" )
                # prohibit clicking of pause btn
                self.pause_btn.config(state=tk.DISABLED)
                # self.left_btn.config(state=tk.DISABLED)
                self.right_btn.config(state=tk.DISABLED)
                
            # Count only positive values,
            if count_dwn > 0:
                    self.timer = self.time_win.after(1000, self.update_timer, count_dwn - 1)
        
            else: # Count has finished restart count

                # start countdown again
                self.count_down()

    def play_pause(self):

        if not self.is_count_finished: # not done
            self.is_start_countdown = not self.is_start_countdown # stop count

            # continue countdown
            if self.count_dwn > 0 and self.is_start_countdown:
                self.pause_btn.config(text="PAUSE")
                self.update_timer(self.count_dwn)
            else:
                self.pause_btn.config(text="PLAY")

    # ---------------------------- TIMER RESET ------------------------------- # 
    def reset_timer(self):
        self.is_break = False
        self.is_start_countdown = False
        self.reps = 0
        self.count_dwn = 0
        self.time_win.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text , text="00:00")
            
    # --------------------- SKIP TIMER --------------------------#############
    def skip_countdown(self):
        # update timelist
        self.reset_timer()
        self.start_timer()



    def loop(self):
        self.time_win.mainloop()

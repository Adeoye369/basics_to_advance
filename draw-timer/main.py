import tkinter as tk
from tkinter import ttk
import random as rd
import math


class Draw_app():
    def __init__(self) -> None:
        # Default
        self.angle = 0
        self.time_interval = 0

        self.reps = 0
        self.count_up = 0
        self.count_up_list = []
        self.canvas = None
        self.drawtime_entry = None
        self.timer = None

        # help to know when to switch countdown display
        self.is_break = False 

        self.root = tk.Tk()

        self.root.title("Draw Timer")
        # self.root.geometry("400x400") # draw window
        self.root.config(padx=20, pady=20)

        # Title label
        self.title_label = tk.Label(self.root, text="Draw Timer", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, columnspan=3, sticky="NSEW")
        
        # MENU UI
        self.create_menu_UI()
        # TIMER UI
        self.create_timer_UI()
        # LIST UI
        self.create_durationList_UI()
        ### =================DRAW MENU ===================== ###

        # main loop
        self.root.mainloop()

    def create_menu_UI(self):
        ### ================= MENU FRAME =================== ### 
        # Options Menu Frame
        self.menu_frame = tk.LabelFrame(self.root, text="Menu", padx=10, pady=10)
        self.menu_frame.grid(row=1, column=0, sticky="NSEW")

        # Display the time for the drawing interval
        self.drawtime_label = tk.Label(self.menu_frame, text="Draw Time(min)")
        self.drawtime_entry = tk.Entry(self.menu_frame, width=10)
        self.drawtime_entry.insert(tk.END, string="1")
        self.warning_label = tk.Label(self.menu_frame, text="", fg="red", font=("Arial", 10, "italic"))
        self.drawtime_label.pack()
        self.drawtime_entry.pack()
        self.warning_label.pack()

        # break time between each drawing 
        self.break_val = tk.IntVar()
        self.break_slider = tk.Scale(self.menu_frame, from_=0, to=15, variable=self.break_val, orient=tk.HORIZONTAL)
        self.break_label = ttk.Label(self.menu_frame, text="breaks (sec)" )
        self.break_label.pack()
        self.break_slider.pack(pady=0)

        ### ================ PLAYBACK - FRAME ===================== ###
        # playback Frame
        self.playback_frame = tk.LabelFrame(self.root)
        self.playback_frame.config(padx=10, pady=10)
        
        self.playback_frame.grid(row=2, column=0, sticky="NSEW")
        self.playback_frame.columnconfigure(0, weight=1)

        # Start, Pause and Reset Button
        # --------------------------- USING PACK()
        # self.start_btn = tk.Button(self.playback_frame, text="START").pack(fill=tk.BOTH)
   
        self.start_btn = tk.Button(self.playback_frame, text="START", command=self.start_timer)
        self.start_btn.grid(row=0, column=0, sticky="NSEW")
        self.pause_btn = tk.Button(self.playback_frame, text="PAUSE")
        self.pause_btn.grid(row=1, column=0, sticky="NSEW")
        self.reset_btn = tk.Button(self.playback_frame, text="RESET")
        self.reset_btn.grid(row=2, column=0, sticky="NSEW")

    def create_durationList_UI(self ):
        ### ================ ELAPSED TIME FRAME ============ ###
        self.elap_time_frame = tk.LabelFrame(self.root, text="Elapsed Time", padx=10, pady=10)
        self.elap_time_frame.grid(row=1, column=2, rowspan=2)
        tk.Grid.rowconfigure(self.elap_time_frame, 0, weight=1)

        # Display list of Elapsed time
        self.time_scrollbar = tk.Scrollbar(self.elap_time_frame)
        self.time_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.timelist = tk.Listbox(self.elap_time_frame, yscrollcommand=self.time_scrollbar.set)
        self.timelist.config(width=10, font=("Cursive", 18,"bold"))
        # for i in range(20):
        #     self.timelist.insert(tk.END, f" {i+1:02d} - {rd.randint(1,60):02d}:{rd.randint(1,60):02d}")

        self.timelist.pack(side=tk.LEFT, fill=tk.BOTH)
        self.time_scrollbar.config(command=self.timelist.yview)

    def create_timer_UI(self):
        self.timer_frame_label = tk.LabelFrame(self.root, text="Timer")
        self.timer_frame_label.grid(row=1, column=1, rowspan=2, sticky="NSEW")

        # TIMER LABEL
       # create canvas 
        self.canvas = tk.Canvas(self.timer_frame_label, 
                                width=240, height=240,
                                 highlightthickness=0)
        
        self.canvas.config(bg="#f7f5dd", highlightthickness=0)
        self.canvas.grid(row=1, column=1)

        self.canvas_text()
        self.canvas_circular_progress()

        # Skip Label
        self.skip_button = tk.Button(self.timer_frame_label, text="SKIP TO NEXT")
        self.skip_button.grid(row=2, column=1, sticky="S", padx=20, pady=20)

    def canvas_text(self):
        self.timer_text = self.canvas.create_text(120, 120, text="00:00", fill="brown", font=("Courier", 50, "bold" ))
        
    def canvas_circular_progress(self):
        self.width = self.canvas.winfo_reqwidth()
        self.height = self.canvas.winfo_reqheight()
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        self.radius = min(self.center_x, self.center_y) - 5

        self.pos_x = self.center_x - self.radius
        self.pos_y = self.center_y - self.radius
        self.diameter_x = self.center_x + self.radius
        self.diameter_y = self.center_y + self.radius
        self.canvas.create_oval(self.pos_x, self.pos_y, self.diameter_x, self.diameter_y,
                                outline="gray", width=5)

        self.arc = self.canvas.create_arc(self.pos_x, self.pos_y, self.diameter_x, self.diameter_y, 
                                          start=0, extent=0, outline="gray", 
                                          width=5, style=tk.ARC)
        
    def get_and_validate_drawtime(self):
        '''
        Check if the draw time is valid value or through 
        Valuerror warning if failed
        @return int value
        '''
        default_entry = 30
        try:
            entry_value = self.drawtime_entry.get()

            if(entry_value == ""): 
                self.warning_label.config(text = "Time is empty, will use default")
                return default_entry
             
            entry_value = int(float(entry_value) * 60)

            if(entry_value == 0): 
                self.warning_label.config(text = "Zero value, will use default")
                return default_entry

        except ValueError:
            self.warning_label.config(text = "Invalid Input, will use default")
            return default_entry

        # All is good, Reset the warning label,
        self.warning_label.config(text = "")

        return entry_value 


    def start_timer(self):

        # set the initial time interval conversion
        self.init_time_interval = self.get_and_validate_drawtime()

        if(self.time_interval < 0):
            self.warning_label.config(text = "Time to small")
            return

        # clear warning
        self.warning_label.config(text = "")

        # start first countdown
        self.count_down()

    '''
    Count down timer =====================
    
    '''
    def count_down(self):

        # get the value assigned to slider
        self.short_break_sec = self.break_val.get()
        self.draw_time_min = self.get_and_validate_drawtime()
        self.reps += 1

        # switch between `initial time interval` and `break time interval`
        if self.reps %2 == 0 and self.short_break_sec != 0:
            self.is_break = True
            self.time_interval = self.short_break_sec
            self.update_timer(self.time_interval)

        else :
            self.is_break = False
            self.time_interval = self.draw_time_min
            self.update_timer(self.time_interval)
        


    def min_sec(self, count):
        return count // 60, count % 60

    def update_count_up(self):
        self.count_up = self.count_up - 1 # offset by 1 error
        self.count_up_list.append(self.count_up)
        self.timelist.insert(tk.END, f" {len(self.count_up_list):02d} - {self.min_sec(self.count_up)[0]:02d}:{self.min_sec(self.count_up)[1]:02d}")
        self.count_up = 0

    '''
    update timer =========================================================
    '''
    def update_timer(self, count):

        # update timer text
        self.min, self.sec = self.min_sec(count)

        # update canvas circle
        self.angle = math.floor((count/self.time_interval)*359)
        # print(self.angle)
        if self.angle < 0: self.angle = 360 # Reset if completed circle
        self.canvas.itemconfig(self.arc, extent=self.angle, outline="blue" if self.angle >= 30 else "red")
        
        if not self.is_break:
            # Update canvas text normal interval
            self.count_up += 1
            self.canvas.itemconfig(self.timer_text, text=f"{self.min:02d}:{self.sec:02d}" )
        else:    
            # Update canvas text for break time
            self.canvas.itemconfig(self.timer_text, text=f"{self.sec}" )
            
        # Count only positive values
        if count > 0:
            self.timer = self.root.after(1000, self.update_timer, count - 1)
       
        else: # Count has finished restart count

            # Store and Display the count_up value 
            if not self.is_break: self.update_count_up()

            # start countdown again
            self.count_down()


if __name__ == "__main__":
    Draw_app()


    


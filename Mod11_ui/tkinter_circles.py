from tkinter import *

class MyApp(object):
    def __init__(self, parent):
        ## This method is internal to the initializer method
        ## and is used for creating buttons. It shortens the program code
        def new_button(parent, cmd, buttontext, packlocation):
            button = Button(parent, command=cmd)
            button.configure(text=buttontext)
            button.configure(width=button_width,
                  padx=button_padx, pady=button_pady )
            button.pack(side=packlocation)
            return button

        #------ constants for controlling layout ------
        button_width = 10
        button_padx = "2m"
        button_pady = "1m"
        buttons_frame_padx =  "3m"
        buttons_frame_pady =  "2m"
        buttons_frame_ipadx = "3m"
        buttons_frame_ipady = "1m"
        # -------------- end constants ----------------

        #---------variables for controlling the function-----
        self.canvas_dimension = 600 ##Canvas will be a square
        self.wait_time = 8
        self.repetitions = 2
        #----------end of variables--------------------------

        self.myParent = parent
        self.main_frame = Frame(parent)
        self.main_frame.pack ()

        ## Two frames inside the main frame, one for the canvas
        ## on top and the second one for buttons in the bottom
        self.draw_frame = Frame(self.main_frame)
        self.draw_frame.pack(side=TOP)

        self.info_canvas = Canvas(self.draw_frame, height=20,
                                   width=self.canvas_dimension)
        self.info_canvas.pack(side=TOP)
        self.text_area = self.info_canvas.create_text(10,10,anchor='nw')
        self.info_canvas.itemconfigure(self.text_area,text="#circles = {:d}".format(self.repetitions))

        self.main_canvas = Canvas(self.draw_frame, \
                                  height=self.canvas_dimension,
                                  width=self.canvas_dimension)
        self.main_canvas.pack()

        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(side=BOTTOM)

        self.draw_button = new_button(self.button_frame,self.draw, 'Draw', LEFT)
        self.clear_button = new_button(self.button_frame,self.clear, 'Clear', LEFT)
        self.increase_button = new_button(self.button_frame,self.increase, 'Increase', LEFT)
        self.reduce_button = new_button(self.button_frame,self.reduce, 'Reduce', LEFT)
        self.quit_button = new_button(self.button_frame,self.quit, 'Quit', RIGHT)

    def clear(self):
        self.main_canvas.delete("all")

    def reduce(self):
        if self.repetitions > 1:
            self.repetitions //= 2
        self.put_info()

    def increase(self):
        if self.repetitions < 200:
            self.repetitions *= 2
        self.put_info()

    def put_info(self):
        ## Change the text field in the canvas
        self.info_canvas.itemconfigure(self.text_area,text="#circles = {:d}".format(self.repetitions))

    def draw(self):
        boundary_offset = 2
        max_radius = (self.canvas_dimension - 2*boundary_offset) // 2
        xc = self.canvas_dimension//2 + boundary_offset
        r = max_radius/self.repetitions
        inc = r
        for i in range(self.repetitions):
            self.main_canvas.create_oval((xc-r, xc-r, xc+r, xc+r))
            r += inc
            self.main_canvas.update() # Actually refresh the drawing on the canvas.
            # Pause execution.  This allows the eye to catch up
            self.main_canvas.after(self.wait_time)

    def quit(self):
        self.myParent.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("Drawing a circle") ##Give a title to the program
    myapp = MyApp(root)
    root.mainloop()
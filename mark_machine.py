##################################################
# Mark Machine - written by Andrew Mengede 2020  #
# given a maximum classwork and homework grade,  #
# displays percentages in an easy to read format #
# requires python 3.6 or later for f string      #
# support.                                       #
# Free to use and redistribute.                  #
##################################################
from tkinter import *
import os

#main screen controller
class menu:
    def __init__(self):
        main_screen = Tk()
        main_screen.title("Mark Machine")
        #set root directory
        dirname = os.path.dirname(__file__)
        image_path = os.path.join(dirname,'img/mark.png')
        top_frame = Frame(main_screen)
        mid_frame = Frame(main_screen)
        left_frame = Frame(mid_frame)
        right_frame = Frame(mid_frame)
        bottom_frame = Frame(main_screen)
        cw_frame = Frame(right_frame)
        hw_frame = Frame(right_frame)

        title = Label(top_frame,text="Mark Machine: grade calculator")

        decoration = Canvas(left_frame,width=284,height=298)
        img = PhotoImage(file=image_path)
        decoration.create_image(0,0,anchor=NW,image=img)

        cw_label = Label(cw_frame,text="Maximum classwork grade:")
        self.cw_input = Entry(cw_frame)
        
        hw_label = Label(hw_frame,text="Maximum homework grade:")
        self.hw_input = Entry(hw_frame)

        calc = Button(bottom_frame,text="Calculate Percentages",command=self.load_report)

        title.pack()
        decoration.pack()
        cw_label.pack(side='left')
        self.cw_input.pack(side='left')
        hw_label.pack(side='left')
        self.hw_input.pack(side='left')
        calc.pack()

        top_frame.pack()
        cw_frame.pack(pady=(0,50))
        hw_frame.pack(pady=(50,0))
        left_frame.pack(side='left')
        right_frame.pack(side='left')
        mid_frame.pack()
        bottom_frame.pack()
        mainloop()

    #load up the report of percentages
    def load_report(self):
        cw_max = int(eval(self.cw_input.get()))
        hw_max = int(eval(self.hw_input.get()))
        report = report_screen(cw_max,hw_max)

class report_screen:
    def __init__(self,cw_max,hw_max):
        report_window = Toplevel()
        report_window.title("Percentages")
        cw_frame = Frame(report_window)
        cw_display = Text(cw_frame,width=40)
        hw_frame = Frame(report_window)
        hw_display = Text(hw_frame,width=40)

        cw_display.insert(END,f"Maximum Classwork grade: {cw_max}\n")
        counter = 0
        while counter<cw_max:
            cw_display.insert(END,f"{counter}:\t{int(100*counter/cw_max)}%\t\t"+f"{counter+0.5}:\t{int(100*(counter+0.5)/cw_max)}%\n")
            counter += 1
        
        hw_display.insert(END,f"Maximum Homework grade: {hw_max}\n")
        counter = 0
        while counter<hw_max:
            hw_display.insert(END,f"{counter}:\t{int(100*counter/hw_max)}%\t\t"+f"{counter+0.5}:\t{int(100*(counter+0.5)/hw_max)}%\n")
            counter += 1

        cw_display.pack()
        hw_display.pack()
        cw_frame.pack(side='left')
        hw_frame.pack(side='left')
        mainloop()

#create menu
menu()

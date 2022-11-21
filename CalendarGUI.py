#importing tkinter module
from tkinter import *

#importing calendar module
import calendar

#create GUI for Calender
def showCalendar():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar for the year")
    gui.geometry("700x800")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1, padx=20)
    gui.mainloop()

#create interface layout for displaying calender
new = Tk()
new.config(background='black')
new.title("Calendar")
new.geometry("250x140")
cal = Label(new, text="Calendar",bg='grey',font=("times", 28, "bold"))
year = Label(new, text="Enter year", bg='dark grey')
year_field=Entry(new)
button = Button(new, text='Show Calendar',fg='Black',bg='Blue',command=showCalendar)


#putting widgets in position
cal.grid(row=1, column=1)
year.grid(row=2, column=1)
year_field.grid(row=3, column=1)
button.grid(row=4, column=1)
new.mainloop()

# pip install tkcalendar
from tkinter import Tk, Button, Label
from tkcalendar import Calendar
from datetime import datetime



class MyCalendar(Calendar):
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day 
    def __init__(self, master):
        super().__init__(master, selectmode="day"
                                        , year=MyCalendar.year
                                        , moth=MyCalendar.month
                                        , day=MyCalendar.day
                                        , cursor="hand1")



if __name__ == "__main__":
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day 
    print(f"{year =} {type(year)}")

    root=Tk()
    root.title('Calender')
    root.geometry("600x400")

    cal = MyCalendar(root)
    cal.grid(column=2, row=0)


    def grab_date():
        pick_date=cal.get_date()
        mylbl.config(text=pick_date)
        print(type(pick_date))
    

    mybtn = Button(root, text="Get Date", command=grab_date)
    mybtn.grid(column=1, row=1, pady=20)

    mylbl = Label(root, text="")
    mylbl.grid(column=2, row=2,pady=20)

    root.mainloop()


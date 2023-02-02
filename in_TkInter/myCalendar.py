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
                                        , cursor="hand1"
                                        , locale= "pl_PL")

    def take_date(self)-> str:
        date_from_calendar = self.get_date()
        print(f"{date_from_calendar =}")
        date_format = "%d.%m.%Y"
        new_date_format = "%Y-%m-%d" # for SQLite format
        parsed_date_format = datetime.strptime(date_from_calendar, 
                                                date_format) # string -> datetime object
        formatted_date = parsed_date_format.strftime(new_date_format) # datetime -> string
        
        return formatted_date

if __name__ == "__main__":
    root=Tk()
    root.title('Calender')
    root.geometry("600x400")

    cal = MyCalendar(root)
    cal.grid(column=2, row=1)
    print(cal.take_date())


    def grab_date():
        date_from_calendar=cal.get_date()
        mylbl.config(text= date_from_calendar)
        print(type( date_from_calendar),  date_from_calendar)
        print("-----------------")
        date_format = "%d.%m.%Y"
        new_date_format = "%Y-%m-%d"
        parsed_date = datetime.strptime(date_from_calendar, date_format)
        print(parsed_date, type(parsed_date))
        print("-----------------")
        formatted_date = parsed_date.strftime(new_date_format)
        print(formatted_date, type(formatted_date))
    

    mybtn = Button(root, text="Get Date", command=grab_date)
    mybtn.grid(column=1, row=2, pady=20)

    mylbl = Label(root, text="")
    mylbl.grid(column=2, row=3,pady=20)

    root.mainloop()


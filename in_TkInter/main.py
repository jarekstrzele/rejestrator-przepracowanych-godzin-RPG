import tkinter as tk
from myCalendar import MyCalendar
from databaseSqlite import MySQLiteDB

class Main(tk.Tk):
    main_frame_color = "#039be5"
    input_frame_color = "#4dd0e1"
    output_frame_color = "#4d9eee"

    
    def __init__(self):
        super().__init__()
        self.title("Rejestrator przepracowanych godzin - RPG")
        self.geometry("800x600")

        ## create frames
        self.main_frame = tk.Frame(self)
        self.main_frame.config(background=Main.main_frame_color)
        
        self.input_frame = tk.LabelFrame(self.main_frame , text="Wprowadzanie godzin oraz daty")
        self.input_frame.config(font=("Arial", 13), background=Main.input_frame_color)
        self.output_frame = tk.LabelFrame(self.main_frame , text="Twoje przepracowane godziny")
        self.output_frame.config(font=("Arial",13), background=Main.output_frame_color)
        self.create_widgets()
        self.start_db()
    
    def create_widgets(self):
        tk.Label(self.output_frame, text="output").grid(row=0, column=0)
        
        # INPUT
        my_font = ("Arial", 12)
        tk.Label(self.input_frame, text="input").pack(pady=10)
        
        ## hours
        lbl_hours = tk.Label(self.input_frame, text="Wpisz godziny")
        lbl_hours.config(font=my_font+("bold",), background=Main.input_frame_color, fg="#01579b" )
        lbl_hours.pack(pady=2)
        self.spbox = tk.Spinbox(self.input_frame, from_=0, to=24, increment=0.5)
        self.spbox.config(font=my_font)
        self.spbox.pack(pady=10)
        
        ## date
        tk.Label(self.input_frame, text=" ", background=Main.input_frame_color).pack(pady=5)
        lbl_date = tk.Label(self.input_frame, text="Wybierz datę")
        lbl_date.config(font=my_font+("bold",), background=Main.input_frame_color, fg="#01579b")
        lbl_date.pack(pady=2)
        self.cal =MyCalendar(self.input_frame)
        self.cal.pack(pady=5)
        
        ## Klawisz zatwierdzający
        tk.Label(self.input_frame, text=" ", background=Main.input_frame_color).pack(pady=5)
        self.btn = tk.Button(self.input_frame, text="Zatwierdź dane", command=self.send_date)
        self.btn.config(font=my_font+("bold",)
                    , background="#01579b"
                    , foreground="white"
                    , activebackground="#42a5f5"
                    , activeforeground="white"
                    , width=15, height=3)
        self.btn.pack(pady=10)
        
        
        
        
        
        
        self.generate_layouts()

    def generate_layouts(self):
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)
        self.input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10 )
        self.output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    def send_date(self):
        my_hours = float(self.spbox.get())
        my_date = self.cal.take_date()        
        self.myDB.insert_data(my_hours, my_date)


    def start_db(self):
        self.myDB = MySQLiteDB() 


if __name__ == "__main__":
    main = Main()

    main.mainloop()



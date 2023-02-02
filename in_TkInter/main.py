import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rejestrator Przepracowanych godzin")
        self.geometry("800x600")

        self.create_widgets()
    
    def create_widgets(self):
        ## create frames
        self.main_frame = tk.Frame(self)
        
        self.input_frame = tk.LabelFrame(self.main_frame , text="Wprowadzanie daty i godzin")
        
        self.output_frame = tk.LabelFrame(self.main_frame , text="Twoje przepracowane godziny")
        tk.Label(self.input_frame, text="input").pack()
        tk.Label(self.output_frame, text="output").pack()
        self.generate_layouts()

    def generate_layouts(self):
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        self.output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)






if __name__ == "__main__":
    main = Main()

    main.mainloop()



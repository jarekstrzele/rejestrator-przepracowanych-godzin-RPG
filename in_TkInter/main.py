from tkinter import Tk

class Main(Tk):
    def __init__(self):
        super().__init__()
        self.title("Rejestrator Przepracowanych godzin")
        self.geometry("800x600")




if __name__ == "__main__":
    main = Main()

    main.mainloop()



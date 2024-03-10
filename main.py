from tkinter import *
from tkinter import ttk

class MainApp:

    def __init__(self):
        self.app = Tk()

        self.app.title("Project Tracker")
        self.app.resizable(width=False, height=False)

        pass

    def run(self):
        self.app.mainloop()

app = MainApp()

app.run()

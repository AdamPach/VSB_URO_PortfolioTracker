from tkinter import *
from tkinter import ttk


class MainApp:

    def __init__(self):
        self.app = Tk()

        self.app.title("Project Tracker")
        self.app.resizable(width=False, height=False)

        self._init_Treeview()

    def _init_Treeview(self):
        self.main_treeview = ttk.Treeview(self.app,
                                          columns=(
                                              "id",
                                              "amount",
                                              "crypto_currency",
                                              "fiat_currency",
                                              "fiat_prise",
                                              "date"),
                                          show='headings')

        self.main_treeview.heading("id", text="ID")
        self.main_treeview.column("id", width=100)

        self.main_treeview.heading("amount", text="Amount")
        self.main_treeview.column("amount", width=100)

        self.main_treeview.heading("crypto_currency", text="Crypto Currency")
        self.main_treeview.column("crypto_currency", width=100)

        self.main_treeview.heading("fiat_currency", text="Fiat Currency")
        self.main_treeview.column("fiat_currency", width=100)

        self.main_treeview.heading("fiat_prise", text="Fiat Price")
        self.main_treeview.column("fiat_prise", width=100)

        self.main_treeview.heading("date", text="Date")
        self.main_treeview.column("date", width=100)

        self.main_treeview.grid(row=0, column=0)

    def run(self):
        self.app.mainloop()


app = MainApp()

app.run()

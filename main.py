from tkinter import *
from tkinter import ttk


class MainApp:

    def __init__(self):
        self.root = Tk()

        self.root.title("Project Tracker")
        self.root.resizable(width=False, height=False)

        self.app = Frame(self.root)

        self._init_Treeview()
        self._init_notebook_menu()

        self.app.pack(pady=25, padx=25)

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

        self.main_treeview.pack(side=LEFT, fill=BOTH, padx=(0, 20))

    def _init_notebook_menu(self):
        self.notebook = ttk.Notebook(self.app)
        self.notebook.pack(side=RIGHT, fill=BOTH, padx=(20, 0))

        self._init_insert_form()

    def _init_insert_form(self):
        self.new_record_notebook_tab = ttk.Frame(self.notebook, height=400, width=300)

        self.notebook.add(self.new_record_notebook_tab, text="New record")

        self.new_record_form = ttk.Frame(self.new_record_notebook_tab)

        self.amount_label = ttk.Label(self.new_record_form, text="Amount")
        self.amount_insert = ttk.Entry(self.new_record_form, width=40)

        FORM_SPACING = (15, 0)

        self.amount_label.grid(row=0, pady=FORM_SPACING, sticky=W)
        self.amount_insert.grid(row=1, sticky=NSEW)

        self.crypto_currency_label = ttk.Label(self.new_record_form, text="Crypto Currency")
        self.crypto_currency_select = ttk.Combobox(self.new_record_form, values=["BTC", "ETH", "LTC"], width=40)

        self.crypto_currency_label.grid(row=2, pady=FORM_SPACING, sticky=W)
        self.crypto_currency_select.grid(row=3, sticky=NSEW)

        self.fiat_currency_label = ttk.Label(self.new_record_form, text="Fiat Currency")
        self.fiat_currency_select = ttk.Combobox(self.new_record_form, values=["CZK", "USD", "EUR"], width=40)

        self.fiat_currency_label.grid(row=4, pady=FORM_SPACING, sticky=W)
        self.fiat_currency_select.grid(row=5, sticky=NSEW)

        self.prise_label = ttk.Label(self.new_record_form, text="Prise")
        self.prise_insert = ttk.Entry(self.new_record_form, width=40)

        self.prise_label.grid(row=6, pady=FORM_SPACING, sticky=W)
        self.prise_insert.grid(row=7, sticky=NSEW)

        self.date_label = ttk.Label(self.new_record_form, text="Date")
        self.date_insert = ttk.Entry(self.new_record_form, width=40)

        self.date_label.grid(row=8, pady=FORM_SPACING, sticky=W)
        self.date_insert.grid(row=9, sticky=NSEW)

        self.add_record_button = ttk.Button(self.new_record_form, text="Add record")
        self.add_record_button.grid(row=10, column=0, pady=(20, 0))

        self.new_record_form.pack(fill=BOTH, padx=25, pady=10)

    def run(self):
        self.root.mainloop()


app = MainApp()

app.run()

from tkinter import *
from tkinter import ttk, messagebox

CRYPTO_CURRENCIES = ["BTC", "ETH", "LTC"]
FIAT_CURRENCIES = ["CZK", "USD", "EUR"]


class CryptoRecord:

    def __init__(self, record_id, amount, crypto_currency, fiat_currency, fiat_price, date):
        self.record_id = record_id
        self.amount = amount
        self.crypto_currency = crypto_currency
        self.fiat_currency = fiat_currency
        self.fiat_price = fiat_price
        self.date = date

    def is_valid(self):

        try:
            float(self.amount)
            float(self.fiat_price)
        except ValueError:
            return False

        if self.fiat_currency not in FIAT_CURRENCIES or self.crypto_currency not in CRYPTO_CURRENCIES:
            return False

        return True


class MainApp:

    def __init__(self):
        self.root = Tk()

        self.root.title("Project Tracker")
        self.root.resizable(width=False, height=False)

        self.app = Frame(self.root)

        self._init_Treeview()
        self._init_notebook_menu()
        self._init_menu()

        self.selected_record = None

        self.records = []

        self.app.pack(pady=25, padx=25)

    def _init_Treeview(self):
        self.main_treeview = ttk.Treeview(self.app,
                                          columns=(
                                              "id",
                                              "amount",
                                              "crypto_currency",
                                              "fiat_currency",
                                              "fiat_price",
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

        self.main_treeview.heading("fiat_price", text="Fiat Price")
        self.main_treeview.column("fiat_price", width=100)

        self.main_treeview.heading("date", text="Date")
        self.main_treeview.column("date", width=100)

        self.main_treeview.bind("<<TreeviewSelect>>", self.item_clicked)

        self.main_treeview.pack(side=LEFT, fill=BOTH, padx=(0, 20))

    def item_clicked(self, event):
        selected_item = self.main_treeview.focus()

        if selected_item == '':
            return

        if selected_item == self.selected_record:
            decision = messagebox.askyesno("Delete Record", "Are you sure you want to")
            if not decision:
                return

            record_id = self.main_treeview.item(self.selected_record)['values'][0]
            new_arr = []

            for record in self.records:
                if record.record_id != record_id:
                    new_arr.append(record)

            self.records = new_arr

            self._add_records()
        else:
            self.selected_record = selected_item

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
        self.crypto_currency_select = ttk.Combobox(self.new_record_form, values=CRYPTO_CURRENCIES, width=40)

        self.crypto_currency_label.grid(row=2, pady=FORM_SPACING, sticky=W)
        self.crypto_currency_select.grid(row=3, sticky=NSEW)

        self.fiat_currency_label = ttk.Label(self.new_record_form, text="Fiat Currency")
        self.fiat_currency_select = ttk.Combobox(self.new_record_form, values=FIAT_CURRENCIES, width=40)

        self.fiat_currency_label.grid(row=4, pady=FORM_SPACING, sticky=W)
        self.fiat_currency_select.grid(row=5, sticky=NSEW)

        self.price_label = ttk.Label(self.new_record_form, text="Price")
        self.price_insert = ttk.Entry(self.new_record_form, width=40)

        self.price_label.grid(row=6, pady=FORM_SPACING, sticky=W)
        self.price_insert.grid(row=7, sticky=NSEW)

        self.date_label = ttk.Label(self.new_record_form, text="Date")
        self.date_insert = ttk.Entry(self.new_record_form, width=40)

        self.date_label.grid(row=8, pady=FORM_SPACING, sticky=W)
        self.date_insert.grid(row=9, sticky=NSEW)

        self.add_record_button = ttk.Button(self.new_record_form, text="Add record", command=self.add_record)
        self.add_record_button.grid(row=10, column=0, pady=(20, 0))

        self.new_record_form.pack(fill=BOTH, padx=25, pady=10)

    def _init_menu(self):
        self.top_menu_bar = Menu(self.root)

        self.settings_menu = Menu(self.top_menu_bar, tearoff=0)

        self.top_menu_bar.add_cascade(label="Settings", menu=self.settings_menu)

        self.settings_menu.add_command(label="Quit", command=self.root.quit)

        self.root.config(menu=self.top_menu_bar)

    def add_record(self):
        record_id = 1 if len(self.main_treeview.get_children()) == 0 else self.main_treeview.item(self.main_treeview.get_children()[-1])['values'][0] + 1
        amount = self.amount_insert.get()
        crypto_currency = self.crypto_currency_select.get()
        fiat_currency = self.fiat_currency_select.get()
        fiat_price = self.price_insert.get()
        date = self.date_insert.get()

        new_record = CryptoRecord(record_id, amount, crypto_currency, fiat_currency, fiat_price, date)

        if not new_record.is_valid():
            messagebox.showerror("Invalid Record", "Invalid record. Please check the input values.")
            return

        self.records.append(new_record)

        self._add_records()

        self.amount_insert.delete(0, END)
        self.crypto_currency_select.delete(0, END)
        self.fiat_currency_select.delete(0, END)
        self.price_insert.delete(0, END)
        self.date_insert.delete(0, END)

    def _add_records(self):

        for i in self.main_treeview.get_children():
            self.main_treeview.delete(i)

        for record in self.records:
            self.main_treeview.insert("", "end", values=(
                record.record_id, record.amount, record.crypto_currency, record.fiat_currency,
                record.fiat_price, record.date))

    def run(self):
        self.root.mainloop()


app = MainApp()

app.run()

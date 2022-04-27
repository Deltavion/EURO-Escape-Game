from tkinter import *


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("EURO Escape")
        self.root.geometry(f"1280x720")
        self.root.resizable(width=True, height=True)

    def create_app(self):
        scrollbar = Scrollbar(self.root)
        scrollbar.grid(row=0, column=1, sticky="nse")

        prompt = Listbox(self.root, yscrollcommand = scrollbar.set,  borderwidth="1px", relief="groove", justify="left")
        prompt.grid(row=0, column=0, sticky='nwse')

        scrollbar.config(command = prompt.yview)

        entry = Entry(self.root)
        entry.grid(row=1, column=0, columnspan=2, sticky='wse')



        self.root.grid_columnconfigure(index=0, weight=1)
        self.root.grid_rowconfigure(index=0, weight=1)


app = App()
app.create_app()
app.root.mainloop()

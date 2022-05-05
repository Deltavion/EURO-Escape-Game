from tkinter import *


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("EURO Escape")
        self.root.geometry(f"1280x720")
        # self.root.attributes('-fullscreen', True)
        self.root.resizable(width=True, height=True)

    def create_app(self):
        # =============================================================objects
        scrollbar = Scrollbar(self.root)
        self.prompt = Listbox(self.root,
                              yscrollcommand=scrollbar.set,
                              borderwidth="1px",
                              relief="groove",
                              background="#222222",
                              foreground="#00ff00",
                              justify="left")
        self.entry = Entry(self.root)
        self.send = Button(self.root,
                           command=self.writeNewLine
                           )

        # =============================================================griding
        scrollbar.grid(column=2, row=0, sticky='nse', ipadx=0, ipady=0)
        self.prompt.grid(column=0, row=0, columnspan=2, sticky='nwse')
        self.entry.grid(column=0, row=1, sticky='nwse', padx=20, pady=15)
        self.send.grid(column=1, row=1,columnspan=2,  sticky='se', padx=15, pady=15, ipadx=50)

        # .grid(row, column, rowspan, columnspan, sticky='wse', ipadx, ipady)

        # ==============================================================config
        self.root.grid_columnconfigure(index=0, weight=1)
        self.root.grid_rowconfigure(index=0, weight=1)


        scrollbar.config(command=self.prompt.yview)

    def cmdStart(self):
        self.prompt.insert('end', "Jacques Chirac spaceship console")
        self.prompt.insert('end', '"The Console"')
        self.prompt.insert('end', ">>>")

    def writeNewLine(self):
        line = self.entry.get()
        self.entry.delete(0, "end")
        self.prompt.insert('end', line)


app = App()
app.create_app()
app.cmdStart()
app.root.mainloop()
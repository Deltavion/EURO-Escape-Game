import tkinter as tk

root = tk.Tk()

tk.Label(text='A', bg='blue').grid(row=0, column=0, sticky='nwse')
root.grid_columnconfigure(index=0, weight=1)
root.grid_rowconfigure(index=0, weight=1)

tk.mainloop()
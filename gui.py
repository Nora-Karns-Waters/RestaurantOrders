from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("960x540")
frame = Frame(root)
frame.pack()

tabControl = ttk.Notebook(root)
create = Frame(tabControl)
view = Frame(tabControl)

tabControl.add(create, text='Create/Edit')
tabControl.add(view, text='Order Tracker')
tabControl.pack(expand=1, fill="both")

root.title("Marigold Orders")
root.mainloop()

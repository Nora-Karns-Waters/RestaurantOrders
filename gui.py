from tkinter import *
from tkinter import ttk
import guifunc as util

newLayoutText = "<-- New Layout -->"


def layoutcallback(selection):
    if selection == newLayoutText:
        print("Test")
        valueInside.set('a')


root = Tk()
root.geometry("960x540")
frame = Frame(root)

# Create option menu for layouts
values = util.get_layouts()
values.append(newLayoutText)
valueInside = StringVar(root)
valueInside.set("Select a Layout")
optionMenu = OptionMenu(frame, valueInside, *values, command=layoutcallback)
optionMenu.pack()

frame.pack()

tabControl = ttk.Notebook(root)
create = Frame(tabControl)
view = Frame(tabControl)

tabControl.add(create, text='Create/Edit')
tabControl.add(view, text='Order Tracker')
tabControl.pack(expand=1, fill="both")

root.title("Marigold Orders")
root.mainloop()


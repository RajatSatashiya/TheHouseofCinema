

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkbox")
root.iconbitmap("C:/Users/Aishwarya/Desktop/Programming/Python learning for projects/garlic.ico")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()
c = Checkbutton(root,text="Click1",variable=var,onvalue="ON",offvalue="OFF")
c.deselect()
c.pack()


button = Button(root,text="Show selection", command=show).pack()


root.mainloop()

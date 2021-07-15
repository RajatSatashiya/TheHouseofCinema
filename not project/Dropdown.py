

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Dropdown")
root.iconbitmap("C:/Users/Aishwarya/Desktop/Programming/Python learning for projects/garlic.ico")
root.geometry("400x400")

def show():
    mylabel = Label(root,text=clicked.get()).pack()
    
options=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root,clicked, *options)
drop.pack()

button = Button(root,text="Show selection", command=show)
button.pack()

root.mainloop()



from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Windows")
root.iconbitmap("C:/Users/Aishwarya/Desktop/Programming/Python learning for projects/garlic.ico")

img = ImageTk.PhotoImage(Image.open("Images/2011.jpg"))

def open():
    top = Toplevel()
    top.title("Top Window")
    label = Label(top,image=img).pack()
    close = Button(top,text="Close",command=top.destroy).pack()

    
button = Button(root,text="Click to open image window",command=open).pack(anchor=W,padx=20,pady=20)




root.mainloop()

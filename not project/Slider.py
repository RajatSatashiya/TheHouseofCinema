
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")
root.iconbitmap("C:/Users/Aishwarya/Desktop/Programming/Python learning for projects/garlic.ico")
root.geometry("400x400")

verticle = Scale(root, from_=0, to=200)
verticle.pack(anchor=E)

def slide():
    my_label = Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")

horizontal = Scale(root, from_=0, to=800,orient=HORIZONTAL)
horizontal.pack(anchor=S)


    
button = Button(root,text="Click",command=slide).pack()





root.mainloop()

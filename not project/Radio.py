
from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Radio")
root.iconbitmap("C:/Users/Aishwarya/Desktop/Programming/Python learning for projects/garlic.ico")

r = IntVar()
r.set(2)

modes = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text,mode in modes:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root,text=value)
    myLabel.pack()
    
#Radiobutton(root,text="Option 1", variable=r,value=1,command=lambda: clicked(r.get())).pack()
#Radiobutton(root,text="Option 2", variable=r,value=2,command=lambda: clicked(r.get())).pack()


button = Button(root,text="Click Me",command=lambda: clicked(pizza.get())).pack()

root.mainloop()

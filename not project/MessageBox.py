
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title("Message Box")
root.iconbitmap("C:/Users/Aishwarya/Desktop/Programming/Python learning for projects/garlic.ico")

def popup():
    response = messagebox.showinfo("This is a popup","Hello World")
    Label(root,text=response).pack()
    """
    if response==1:
        Label(root,text="You clicked yes").pack()
    else:
        Label(root,text="You cliked no").pack()
    """      
button = Button(root,text="Pop Up",command=popup).pack()


root.mainloop()

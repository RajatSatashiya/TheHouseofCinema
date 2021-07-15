
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Files")
root.iconbitmap("C:/Users/Aishwarya/Desktop/Programming/Python learning for projects/garlic.ico")

def open():
    global img
    a = filedialog.askopenfilename(initialdir="C:/Users/Aishwarya/Desktop/Programming/Python learning for projects/images",title="Select a file",filetypes=(("jpg files","*.jpg"),("all files","*.*")))
    img = ImageTk.PhotoImage(Image.open(a))
    img_label = Label(image=img).pack()

my_button = Button(root,text="Open File", command=open).pack()





root.mainloop()

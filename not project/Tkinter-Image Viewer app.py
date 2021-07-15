
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Images")
root.iconbitmap('C:/Users/Aishwarya/Desktop/Programming/Python learning for projects/garlic.ico')

my_img0 = ImageTk.PhotoImage(Image.open("images/rome.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("images/2011.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/xbox.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/vit.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/vit black.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/sachin.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/Beach.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("images/graffiti.jpg"))

image_list = [my_img0,my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]

status = Label(root,text="Image 1 of " +str(len(image_list)),bd=5,relief=SUNKEN, anchor=E)

my_label = Label(image=my_img0)
my_label.grid(row=0,column=0,columnspan=3)

def forward(img_num):
    global my_label
    global button_back
    global button_forward 
    my_label.grid_forget()
    my_label = Label(image=image_list[img_num - 1])
    button_forward = Button(root,text='>>',command=lambda: forward(img_num + 1))
    button_back = Button(root,text='<<',command=lambda: back(img_num-1))
    if img_num==8:
        button_forward = Button(root, text=">>",state=DISABLED)
    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status = Label(root,text="Image " +str(img_num)+ " of " +str(len(image_list)), bd=5, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)

def back(img_num):
    global my_label
    global button_back
    global button_forward
    my_label.grid_forget()
    my_label = Label(image=image_list[img_num - 1])
    button_forward = Button(root,text='>>',command=lambda: forward(img_num + 1))
    button_back = Button(root,text='<<',command=lambda: back(img_num-1))
    if img_num==1:
        button_back = Button(root,text="<<",state=DISABLED)
        
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status = Label(root,text="Image " +str(img_num)+ " of " +str(len(image_list)),bd=5,relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)


button_back = Button(root, text='<<', command=back,state=DISABLED)
button_exit = Button(root, text='Exit', command = root.destroy)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1,pady=10)
button_forward.grid(row=1,column=2)

status.grid(row=2,column=0,columnspan=3, sticky=W+E)


root.mainloop()
   

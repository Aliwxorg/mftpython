from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("ali rajab asadi")

my_img1=ImageTk.PhotoImage(Image.open('images/snake.png'))
my_img2=ImageTk.PhotoImage(Image.open('images/vipre.png'))
my_img3=ImageTk.PhotoImage(Image.open('images/me2.jpg'))
my_img4=ImageTk.PhotoImage(Image.open('images/me.jpg'))

list_image=[my_img1,my_img2,my_img3,my_img4]

staus=Label(root,text="image 1 of "+ str(len(list_image)),bd=2,relief=SUNKEN,anchor=E)
staus.grid(row=3,column=0,columnspan=3,sticky=W+E)

def forward(img_no):
    global button_exit
    global button_forward
    global button_back
    global my_label
    label = Label(image=list_image[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="forward",command=lambda: forward(img_no + 1))
    button_back = Button(root, text="Back",command=lambda: back(img_no - 1))
    if img_no == 4:
        button_forward = Button(root, text="Forward",state=DISABLED)
    button_back = Button(root, text="Back",
                         command=lambda: back(img_no - 1))
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)
    print(img_no)
    my_label.grid_forget()
    staus = Label(root, text="image "+ str(img_no) +" of " + str(len(list_image)), bd=2, relief=SUNKEN, anchor=E)
    staus.grid(row=3, column=0, columnspan=3, sticky=W + E)

def back(img_no):
    global button_exit
    global button_forward
    global button_back
    global my_label
    label = Label(image=list_image[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="forward",command=lambda: forward(img_no + 1))
    button_back = Button(root, text="Back", command=lambda: back(img_no - 1))
    print(img_no)
    if img_no == 1:
        button_back = Button(root, Text="Back", state=DISABLED)


    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)
    staus = Label(root, text="image "+ str(img_no) +" of " + str(len(list_image)), bd=2, relief=SUNKEN, anchor=E)
    staus.grid(row=3, column=0, columnspan=3, sticky=W + E)

my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

button_exit=Button(root,text="exit program",command=root.quit)
button_forward=Button(root,text=">>",command=lambda:forward(1))
button_back=Button(root,text="<<",command=back,state=DISABLED)

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)




root.mainloop()
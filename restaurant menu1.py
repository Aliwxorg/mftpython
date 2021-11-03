from tkinter import *
root=Tk()
root.title("felfel qermez menu")
pizza=LabelFrame(root,text="pizza",padx=10,pady=10)
pizza.pack()

drinks=LabelFrame(root,text="drinks",padx=10,pady=10)
drinks.pack()

junk_food=LabelFrame(root,text="junk_food",padx=10,pady=10)
junk_food.pack()

food=StringVar()

Radiobutton(pizza,text="peperoni",variable=food,value=1200).pack(anchor=W)
Radiobutton(pizza,text="mix",variable=food,value=800).pack(anchor=W)
Radiobutton(pizza,text="special",variable=food,value=1500).pack(anchor=W)

Radiobutton(drinks,text="soda",variable=food,value=200).pack(anchor=W)
Radiobutton(drinks,text="water",variable=food,value=100).pack(anchor=W)
Radiobutton(drinks,text="lemonad",variable=food,value=300).pack(anchor=W)

Radiobutton(junk_food,text="mushroom",variable=food,value=300).pack(anchor=W)
Radiobutton(junk_food,text="onion",variable=food,value=10).pack(anchor=W)
Radiobutton(junk_food,text="potato",variable=food,value=500).pack(anchor=W)

def choose(value):
    label=Label(root,text=value)
    label.pack()

button=Button(root,text="submit",command=lambda: choose(food.get()))
button.pack()

root.mainloop()
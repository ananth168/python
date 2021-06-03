from tkinter import *

root = Tk()

lable1 = Label(root, text="firstname", fg="black")
lable1.pack(fill=X)
label2 = Label(root, text="lastname", fg="black")
label2.pack(fill=Y)
button1 = Button(root, text="save", fg="white", bg="black")
entry1 = Entry(root)
entry2 = Entry(root)

lable1.grid(row=0, column=0)
label2.grid(row=1, column=0)
button1.grid(row=2, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)


root.mainloop()

from tkinter import *

root = Tk()
myLabel1 = Label(root, text = "Hello World!").grid(row=0,column=0)
myLabel2 = Label(root, text = "Меня зовут Вася Пупкин")
myLabel2.grid(row=1,column=5)
root.mainloop()
from tkinter import *

root = Tk()

e = Entry(root, width=50, bg='blue', fg = "white", borderwidth = 5)
e.pack()
e.insert(0, "Введите ваше имя ")

def myClick():
    hello = "Привет " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text = "Введите ваше имя ", command=myClick, fg="blue", bg="#ffffff")
myButton.pack()

root.mainloop()
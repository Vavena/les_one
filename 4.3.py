from tkinter import *

root = Tk()
def myClick():
    myLabel = Label(root, text="Кнопка нажата")
    myLabel.pack()

myButton = Button(root,text = "Нажмите", command=myClick, fg="blue", bg='#ffffff')
myButton.pack()
root.mainloop()
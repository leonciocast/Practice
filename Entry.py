from tkinter import *

root = Tk()
root.title("Title")

e = Entry(root)
e.pack()
e.insert(0, "Enter your name:")

def MyClick():
    myLabel=Label(root, text=e.get())
    myLabel.pack()


myButton = Button(root, text="What's your name:", command=MyClick)
myButton.pack()

root.mainloop()
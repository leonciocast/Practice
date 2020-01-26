from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

def myClick():

    myLabel = Label(frame, text="I clicked a button!")
    myLabel.pack()


bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text = "Red", fg = "red", command=myClick)
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text = "Brown", fg = "brown", padx=20, pady=20)
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text = "Blue", fg = "blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text = "Black", fg = "black")
blackbutton.pack( side = BOTTOM)

root.mainloop()
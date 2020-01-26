from tkinter import *

root = Tk()

# Creating a Label widget
myLabel = Label(root, text="Leoncio")
myLabel2 = Label(root, text="Castillo")
texto = Label(root, text="Dios es bueno")
# Shoving it onto the screen
#myLabel.pack()



myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
texto.grid(row=2, column=0)
root.mainloop()

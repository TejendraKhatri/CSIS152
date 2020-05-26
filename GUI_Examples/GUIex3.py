from tkinter import *
mainWindow = Tk(); mainWindow.minsize(200,100)
mainWindow.geometry("320x100")

def printMsg():
    print("Hello from Mickey")

imgMickey = PhotoImage(file="mickeymouse1.gif")
btnOK = Button(mainWindow,image=imgMickey, command= printMsg, height=60, width=60)
btnOK.pack()
mainWindow.mainloop()

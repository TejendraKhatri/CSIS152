from tkinter import *
def PrintGreeting():
    print("Hello")

mainWin = Tk(); mainWin.title("Ex Button")
mainWin.minsize(230,200)
mainWin.config()
btn = Button(mainWin, text="Greeting",command = PrintGreeting)
btn.pack()
mainWin.mainloop()

from tkinter import *

mainWin = Tk( )
Label(mainWin, text="Student info").grid(row=0, column=0)
Label(mainWin, text="************").grid(row=1, column=0)
Label(mainWin, text="Name").grid(row=2, column=0)
Label(mainWin, text="John Doe").grid(row=2, column=1)
Label(mainWin, text="Major").grid(row=3, column=0)
Label(mainWin, text="Chemistry").grid(row=3, column=1)
mainWin.mainloop()



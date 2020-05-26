from tkinter import *
def showMsgWin():
    newWin = Toplevel()     ##creating a child window
    newWin.minsize(300,300);   newWin.title("New Window")
    lblMessage = Label(newWin,text="New Window")
    lblMessage.pack()
    btnClose = Button(newWin,text="Close",command=newWin.destroy)
    btnClose.pack()
mainWin = Tk()
mainWin.minsize(500,300)
mainWin.title("Main Window")
btnShow = Button(mainWin, text="New Window",command=showMsgWin)
btnShow.pack()
mainWin.mainloop()

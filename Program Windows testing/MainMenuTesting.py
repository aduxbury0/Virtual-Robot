from tkinter import *
root = Tk()
root.resizable(width=False, height=False)

mainFrame = Frame(root, width=400, height=400, bg="white")
mainFrame.pack()


mainTitle = Text(mainFrame)
mainTitle.insert(END, "Virtual Robot \n Simulator")
mainTitle.pack()

root.mainloop()


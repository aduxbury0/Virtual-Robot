from tkinter import *
root = Tk()
root.resizable(width=False, height=False)

mainFrame = Frame(root, width=800, height=400)
mainFrame.pack()

robotcanvas = Canvas(mainFrame, width=500, height=400, bg="white")
robotcanvas.pack(side="left")
controlFrame = Frame(mainFrame, width=400, height=400, bg="white")
controlFrame.pack(side="right")
root.mainloop()


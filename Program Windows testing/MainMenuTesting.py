from tkinter import *


root = Tk()
root.resizable(width=False, height=False)

mainFrame = Frame(root, height="200", width="200")
mainFrame.pack()

mainTitle = Label(mainFrame, width=60, height=25, bg="white")
# mainTitle = Label(mainFrame, text="Virtual Robot \nProject", width=60, height=25, bg="white")
mainTitle.pack()

startButton = Button(mainFrame, text="Start", width=6, height=2, font="Arial")
startButton.pack()

root.mainloop()
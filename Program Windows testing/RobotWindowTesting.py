from tkinter import *
root = Tk()
root.resizable(width=False, height=False)

mainFrame = Frame(root, width=800, height=400)
mainFrame.pack()

robotcanvas = Canvas(mainFrame, width=500, height=400, bg="white")
robotcanvas.pack(side="left")
# robotcanvas.grid(row="0", column="1")

controlFrame = Frame(mainFrame, width=300, height=400, bg="white")
controlFrame.pack_propagate(0)
controlFrame.pack(side="right")
# controlFrame.grid(row="0", column="2")

inputsFrame = Frame(controlFrame, width=300, height=200, bg="white")
inputsFrame.pack_propagate(0)
# inputsFrame.grid(row="0", column="1")
# inputsFrame.columnconfigure(0, weight="2")
inputsFrame.pack(side="top")

distanceCounterFrame = Frame(controlFrame, width=300, height=200, bg="red")
distanceCounterFrame.pack_propagate(0)
# distanceCounterFrame.grid(row="1", column="1")
# distanceCounterFrame.columnconfigure(0, weight="1")
distanceCounterFrame.pack(side="bottom")

robotSpeedInput = Entry(inputsFrame)
robotSpeedInput.grid(row="0", column="0")
robotSpeedButton = Button(inputsFrame, text="Set Speed")
robotSpeedButton.grid(row="0", column="1")
setDistanceInput = Entry(inputsFrame)
setDistanceInput.grid(row="1", column="0")
distanceInputButton = Button(inputsFrame, text="Set Distance")
distanceInputButton.grid(row="1", column="1")

root.mainloop()


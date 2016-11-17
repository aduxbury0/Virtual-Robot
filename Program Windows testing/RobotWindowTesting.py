from tkinter import *

difficulty = "Virtual Robot Simulator - Easy"
robotDistance = 300000

# This is the main TK window
root = Tk()
root.resizable(width=False, height=False)
root.title(difficulty)

# This is the main frame within the Tk window, it sets the total size of the window
mainFrame = Frame(root, width=800, height=400)
mainFrame.pack()

# This is the left hand side canvas for the robot to move on
robotcanvas = Canvas(mainFrame, width=500, height=400, bg="grey")
robotcanvas.pack(side="left")
robot1 = robotcanvas.create_rectangle(3, 7, 3 + 10, 7 + 10)

# This is the top half of the control inputs, containing the 2 input boxes and buttons
controlFrame = Frame(mainFrame, width=300, height=400, bg="white", pady="10")
controlFrame.pack_propagate(0)
controlFrame.pack(side="right")

# This is the bottom half of the control inputs, containing the start/stop buttons and the label containing the distance
inputsFrame = Frame(controlFrame, width=300, height=200, bg="white")
inputsFrame.pack_propagate(0)
inputsFrame.pack(side="top")

distanceCounterFrame = Frame(controlFrame, width=300, height=200, bg="white", bd="5")
distanceCounterFrame.pack_propagate(0)
distanceCounterFrame.pack(side="bottom")

robotSpeedInput = Entry(inputsFrame)
robotSpeedInput.grid(row="1", column="0")
robotSpeedButton = Button(inputsFrame, text="Set Speed")
robotSpeedButton.grid(row="1", column="1")
setDistanceInput = Entry(inputsFrame)
setDistanceInput.grid(row="4", column="0")
distanceInputButton = Button(inputsFrame, text="Set Distance")
distanceInputButton.grid(row="4", column="1")

startButton = Button(distanceCounterFrame, text="Start")

startButton.grid(row="0", column="0")
stopButton = Button(distanceCounterFrame, text="Stop")
stopButton.grid(row="0", column="1")
distanceLabel = Label(distanceCounterFrame, text="The robot is \n"+ str(robotDistance)+"\n blocks from the end", pady="10", bg="white")
distanceLabel.config(font=("Calibri", 13), relief="sunken", padx="4")
distanceLabel.grid(row="5", column="0", columnspan="2")

root.mainloop()


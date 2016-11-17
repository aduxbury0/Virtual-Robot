from tkinter import *
import time

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
# Initial drawing of the robot block
robot1 = robotcanvas.create_rectangle(3, 7, 3 + 10, 7 + 10)

# This is the frame that contains all of the control inputs on the right hand side of the screen
controlFrame = Frame(mainFrame, width=300, height=400, bg="gray90", pady="10")
controlFrame.pack_propagate(0)
controlFrame.pack(side="right")

# This is the top half of the control inputs, containing the 2 input boxes and buttons
inputsFrame = Frame(controlFrame, width=300, height=200, bg="gray90")
inputsFrame.pack_propagate(0)
inputsFrame.pack(side="top")

# This is the bottom half of the control inputs, containing the start/stop buttons and the label containing the distance
distanceCounterFrame = Frame(controlFrame, width=300, height=200, bg="gray90", bd="5")
distanceCounterFrame.pack_propagate(0)
distanceCounterFrame.pack(side="bottom")

robotSpeedInput = Entry(inputsFrame)
robotSpeedInput.grid(row="1", column="0", padx="5")
robotSpeedButton = Button(inputsFrame, text="Set Speed")
robotSpeedButton.grid(row="1", column="1", sticky="W", padx="5", pady="5")
setDistanceInput = Entry(inputsFrame)
setDistanceInput.grid(row="2", column="0", padx="5")
distanceInputButton = Button(inputsFrame, text="Set Distance")
distanceInputButton.grid(row="2", column="1", padx="5", pady="5")

startButton = Button(distanceCounterFrame, text="Start", padx="10", pady="5")
startButton.grid(row="0", column="0", pady="15")
stopButton = Button(distanceCounterFrame, text="Stop", padx="10", pady="5")
stopButton.grid(row="0", column="1", pady="15")
distanceLabel = Label(distanceCounterFrame, text="The robot is\n" + str(robotDistance)+"\n  blocks from the end  ", pady="10", bg="white")
distanceLabel.config(font=("Arial", 13), relief="groove")
distanceLabel.grid(row="2", column="0", columnspan="2")

root.mainloop()


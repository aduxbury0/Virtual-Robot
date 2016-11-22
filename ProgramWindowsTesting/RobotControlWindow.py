from tkinter import *
import time

difficulty = "Virtual Robot Simulator - Easy"
robotDistance = 300000
roboton = False

# This is the main TK window
root = Tk()
root.resizable(width=False, height=False)
root.title(difficulty)

# This is the main frame within the Tk window, it sets the total size of the window
mainFrame = Frame(root, width=800, height=400)
mainFrame.pack()

# This is the left hand side canvas for the robot to move on
robotcanvas = Canvas(mainFrame, width=500, height=400, bg="white")

# Initial drawing of the robot block
robot1 = robotcanvas.create_rectangle(3, 7, 3 + 10, 7 + 10, fill="white")
wall1 = robotcanvas.create_rectangle(0, 50, 25, 400, fill="grey", outline="grey")
wall2 = robotcanvas.create_rectangle(0, 0, 500, 50, fill="grey", outline="grey")
wall3 = robotcanvas.create_rectangle(475, 50, 500, 400, fill="grey", outline="grey")
wall4 = robotcanvas.create_rectangle(100, 125, 125, 400, fill="grey", outline="grey")
wall5 = robotcanvas.create_rectangle(375, 125, 400, 400, fill="grey", outline="grey")
wall6 = robotcanvas.create_rectangle(125, 300, 375, 400, fill="grey", outline="grey")
wall7 = robotcanvas.create_rectangle(200, 50, 300, 225, fill="grey", outline="grey")
robotcanvas.pack(side="left")


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
stopButton = Button(distanceCounterFrame, text="Stop", padx="10", pady="5", state="disabled")
stopButton.grid(row="0", column="1", pady="15")
distanceLabel = Label(distanceCounterFrame, text="The robot is\n" + str(robotDistance)+"\n  blocks from the end  ", pady="10", bg="white")
distanceLabel.config(font=("Arial", 13), relief="groove")
distanceLabel.grid(row="2", column="0", columnspan="2")


# class Objects:

#    def __init__(self, objectname, xmin, xmax, ymin, ymax, object_type, object_colour):
#        self.objectname = objectname
#        self.xmin = xmin
#        self.xmax = xmax
#        self.ymin = ymin
#        self.ymax = ymax
#        self.type = object_type
#        self.colour = object_colour
#        robotcanvas.create_rectangle(self.xmin, self.ymin, self.xmax, self.ymax, fill=self.colour)

#    def create_object(self):


# wall10 = Objects("Wall 10", 0, 0, 300, 300, "wall", "Red")


def move_object():
    # Boundaries
    vy = 5.0
    vx = 10.0
    x_min = 0.0
    y_min = 0.0
    x_max = 500.0
    y_max = 400.0
    startButton.config(state="disabled")
#    for t in range(1, 500):
    while robot_on == True:
        stopButton.config(state="normal")
        x1, y1, x2, y2 = robotcanvas.coords(robot1)
    # If a boundary has been crossed, reverse the direction
        if x1 >= x_max:
            vx = -10.0
        if y1 <= y_min:
            vy = 5.0
        if y2 >= y_max:
            vy = -5.0
        if x1 <= x_min:
            vx = 10.0
        # Move robot a fixed amount
        robotcanvas.coords(robot1, x1+vx, y1+vy, x2+vx, y2+vy)
        robotcanvas.update()
        time.sleep(0.01)
    startButton.config(state="normal")
    stopButton.config(state="disabled")


def stop_object(robot_on):
    if robot_on:
        robot_on = False
    else:
        robot_on = True
    return robot_on

startButton.config(command=move_object)
stopButton
root.mainloop()
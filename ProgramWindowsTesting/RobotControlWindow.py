from tkinter import *
import time
global robot_on
robot_speed = StringVar

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
robotcanvas = Canvas(mainFrame, width=500, height=400, bg="white")
robotcanvas.pack(side="left")

# Initial drawing of the robot block
robot1 = robotcanvas.create_rectangle(30, 380, 30 + 10, 380 + 10, fill="white")

wall1 = robotcanvas.create_rectangle(0, 50, 25, 400, fill="grey", outline="grey")
wall2 = robotcanvas.create_rectangle(0, 0, 500, 50, fill="grey", outline="grey")
wall3 = robotcanvas.create_rectangle(475, 50, 500, 400, fill="grey", outline="grey")
wall4 = robotcanvas.create_rectangle(100, 125, 125, 400, fill="grey", outline="grey")
wall5 = robotcanvas.create_rectangle(375, 125, 400, 400, fill="grey", outline="grey")
wall6 = robotcanvas.create_rectangle(125, 300, 375, 400, fill="grey", outline="grey")
wall7 = robotcanvas.create_rectangle(200, 50, 300, 225, fill="grey", outline="grey")
finish_line = robotcanvas.create_rectangle(401, 375, 475, 400, fill="grey78", outline="")
robotcanvas.tag_raise(robot1)


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
distanceInputButton = Button(inputsFrame, text="Set Distance", state="disabled")
distanceInputButton.grid(row="2", column="1", padx="5", pady="5")

startButton = Button(distanceCounterFrame, text="Start", padx="10", pady="5")
startButton.grid(row="0", column="0", pady="15")
stopButton = Button(distanceCounterFrame, text="Stop", padx="10", pady="5", state="disabled")
stopButton.grid(row="0", column="1", pady="15")
distanceLabel = Label(distanceCounterFrame, text="The robot is\n" + str(robotDistance)+"\n  blocks from the end  ", pady="10", bg="white")
distanceLabel.config(font=("Arial", 13), relief="groove")
distanceLabel.grid(row="2", column="0", columnspan="2")


def set_speed():
    robot_speed = robotSpeedInput.get()
    print(robot_speed)
    if robot_speed == 1:
        refresh_speed = 0.45
    elif robot_speed == 2:
        refresh_speed = 0.4
    elif robot_speed == 3:
        refresh_speed = 0.35
    elif robot_speed == 4:
        refresh_speed = 0.3
    elif robot_speed == 5:
        refresh_speed = 0.25
    elif robot_speed == 6:
        refresh_speed = 0.2
    elif robot_speed == 7:
        refresh_speed = 0.15
    elif robot_speed == 8:
        refresh_speed = 0.1
    elif robot_speed == 9:
        refresh_speed = 0.05
    else:
        refresh_speed = 0.01
    return refresh_speed


def stop_object():
    robot_on = False
    return robot_on


def object_detection(x1, y1, x2, y2, vx, vy,  colliding_object):
    ox1, oy1, ox2, oy2 = robotcanvas.bbox(colliding_object)
    print(oy1, oy2, ox1, ox2)
    # This rebounds off of the left of objects
    if y1 >= oy1 and y2 <= oy2 and ox1 <= x2 <= ox2:
        vx = -1.0
        vy = vy
        return vx, vy
    # This rebounds off the right side of objects
    elif y1 >= oy1 and y2 <= oy2 and ox2 >= x1 >= ox1:
        vx = 1.0
        vy = vy
        return vx, vy
    # This rebounds off of the bottom of objects
    elif x1 >= ox1 and x2 <= ox2 and oy2 >= y1 >= oy1:
        vy = 1.0
        vx = vx
        return vx, vy
    # This rebounds off the top of objects
    elif x1 >= ox1 and x2 <= ox2 and oy1 <= y2 <= oy2:
        vy = -1.0
        vx = vx
        return vx, vy
    else:
        vy = vy
        vx = vx
        return vx, vy


def finish_detection(x1, y1, x2, y2, colliding_object):
    ox1, oy1, ox2, oy2 = robotcanvas.bbox(colliding_object)
    print(oy1, oy2, ox1, ox2)
    # This rebounds off of the left of objects
    if y1 >= oy1 and y2 <= oy2 and ox1 <= x2 <= ox2:
        finish_message()
        return True
    # This rebounds off the right side of objects
    elif y1 >= oy1 and y2 <= oy2 and ox2 >= x1 >= ox1:
        finish_message()
        return True
    # This rebounds off of the bottom of objects
    elif x1 >= ox1 and x2 <= ox2 and oy2 >= y1 >= oy1:
        finish_message()
        return True
    # This rebounds off the top of objects
    elif x1 >= ox1 and x2 <= ox2 and oy1 <= y2 <= oy2:
        finish_message()
        return True
    else:
        return False


def finish_message():
    finish_popup = Tk()
    finish_popup.title("Done")
    finish_frame = Frame(finish_popup, width=100, height=60)
    finish_frame.pack()
    label = Label(finish_frame, text="The robot is finished!")
    label.pack(side="top", pady=10)
    ok_button = Button(finish_frame, text="Okay", command=finish_popup.destroy)
    ok_button.pack()
    finish_popup.mainloop()


def move_object():
    # Boundaries
    vy = -1.0
    vx = 1.0
    x_min = 0.0
    y_min = 0.0
    x_max = 500.0
    y_max = 400.0
    robot_on = True
    robotcanvas.coords(robot1, 30, 380, 30 + 10, 380 + 10)
    robotcanvas.update()
    refresh_speed = int(set_speed())
    print(refresh_speed)
    startButton.config(state="disabled")
    while robot_on:
        stopButton.config(state="normal")
        x1, y1, x2, y2 = robotcanvas.coords(robot1)
    # If a boundary has been crossed, reverse the direction
        vx, vy = object_detection(x1, y1, x2, y2, vx, vy, wall1)
        vx, vy = object_detection(x1, y1, x2, y2, vx, vy, wall2)
        vx, vy = object_detection(x1, y1, x2, y2, vx, vy, wall3)
        vx, vy = object_detection(x1, y1, x2, y2, vx, vy, wall4)
        vx, vy = object_detection(x1, y1, x2, y2, vx, vy, wall5)
        vx, vy = object_detection(x1, y1, x2, y2, vx, vy, wall6)
        vx, vy = object_detection(x1, y1, x2, y2, vx, vy, wall7)
        if x1 >= x_max:
            vx = -1.0
        if y1 <= y_min:
            vy = 1.0
        if y2 >= y_max:
            vy = -1.0
        if x1 <= x_min:
            vx = 1.0
        if finish_detection(x1, y1, x2, y2, finish_line):
            break
        robotcanvas.coords(robot1, x1+vx, y1+vy, x2+vx, y2+vy)
        robotcanvas.update()
        time.sleep(refresh_speed)
    startButton.config(state="normal")
    stopButton.config(state="disabled")


startButton.config(command=move_object)
stopButton.config(command=stop_object)


root.mainloop()

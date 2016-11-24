from tkinter import *
import time

difficulty = "Virtual Robot Simulator - Easy"
robotDistance = 300000
# This is the main TK window
root = Tk()
root.resizable(width=False, height=False)
root.title(difficulty)
robot_speed_variable = StringVar()

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

speedDescriptionLabel = Label(inputsFrame, text="Enter a number between 1 and 0.01 (1 being slowest)", bg="gray90")
speedDescriptionLabel.grid(row="1", column="0", columnspan=2, padx="5")
robotSpeedInput = Entry(inputsFrame, textvariable=robot_speed_variable)
robotSpeedInput.grid(row="2", column="0", padx="5")
robotSpeedButton = Button(inputsFrame, text="Set Speed")
robotSpeedButton.grid(row="2", column="1", sticky="W", padx="5", pady="5")
setDistanceInput = Entry(inputsFrame)
setDistanceInput.grid(row="3", column="0", padx="5")
distanceInputButton = Button(inputsFrame, text="Set Distance", state="disabled")
distanceInputButton.grid(row="3", column="1", padx="5", pady="5", sticky="w")

startButton = Button(distanceCounterFrame, text="Start", padx="10", pady="5")
startButton.grid(row="0", column="0", pady="15")
stopButton = Button(distanceCounterFrame, text="Stop", padx="10", pady="5", state="disabled")
stopButton.grid(row="0", column="1", pady="15")
distanceLabel = Label(distanceCounterFrame, text="The robot is\n" + str(robotDistance)+"\n  blocks from the end  ", pady="10", bg="white")
distanceLabel.config(font=("Arial", 13), relief="groove")
distanceLabel.grid(row="2", column="0", columnspan="2")


#def set_speed():
#    robot_speed = robot_speed_variable.get
#    print(robot_speed)
#    if robot_speed == str(1):
#        refresh_speed = float(0.45)
#    elif robot_speed == str(2):
#        refresh_speed = float(0.4)
#    elif robot_speed == str(3):
#        refresh_speed = float(0.35)
#    elif robot_speed == str(4):
#        refresh_speed = float(0.3)
#    elif robot_speed == str(5):
#        refresh_speed = float(0.25)
#    elif robot_speed == str(6):
#        refresh_speed = float(0.2)
#    elif robot_speed == str(7):
#        refresh_speed = float(0.15)
#    elif robot_speed == str(8):
#        refresh_speed = float(0.1)
#    elif robot_speed == str(9):
#        refresh_speed = float(0.05)
#    else:
#        refresh_speed = float(0.01)
#    return refresh_speed


# def stop_object():
#    robot_on = False
#    return robot_on

"""This function is used to detect the collisions between the robot and the other static objects in the arena,
it takes 7 arguments -
x1 - is the first x coordinate of the current position of the robot
y1 - is the first y coordinate of the current position of the robot
x2 - is the second x coordinate of the current position of the robot
y2 - is the second y coordinate of the current position of the robot
vx - is the horizontal speed of the robot (+ive number indicates movement toward the far side of the canvas)
vy - is the vertical speed of the robot (+ive number indicates moving towards the bottom of the canvas)
colliding_object is the object on the canvas that is passed into the function

the function then returns a new v value depending on where on the object the robot collides with,
if it collides with nothing then it returns the original vx and vy values that were passed in"""


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


"""This function is used to detect the collisions between the robot and the finish line.
it takes 5 arguments -
x1 - is the first x coordinate of the current position of the robot
y1 - is the first y coordinate of the current position of the robot
x2 - is the second x coordinate of the current position of the robot
y2 - is the second y coordinate of the current position of the robot
colliding_object is the object on the canvas that is passed into the function

the function returns True or False depending on whether is has has hit or not, true for a hit and false for anything else"""


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

"""This function creates a message box with "The robot is finished" as a label on it, and creates a button that
destroys the text box when pressed. It takes no arguments from anywhere else"""


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


"""This is the main looping part of the program, it takes no inputs but:
- it creates variables for the speed of the robot
- it sets the maximum x and y coords of the entire canvas
- sets robot_on to be true so that the while loop will run until it is set to False
- it takes the text written in the speed entry box and then converts it to a standard variable from a stringvar, then
gives it to the sleep function to determin how fast the canvas is redrawn
- it sets the robot coords back to their starting position when the function is called
- it has a while loop that moves the robot while checking for object collisions by calling the object_detection function
- it makes sure the robot does not go out of bounds of the canvas
- it checks to see if the robot has reached the finishing line, and if so then breaks from the loop
- it redraws the robot based on the positions given back by the object_detection and finish_detection functions
- it then waits to start the next iteration of the loop"""


def move_object():
    # Boundaries
    vy = -1.0
    vx = 1.0
    x_min = 0.0
    y_min = 0.0
    x_max = 500.0
    y_max = 400.0
    robot_on = True
#    refresh_speed = set_speed()
    refresh_speed = float(robot_speed_variable.get())
    robotcanvas.coords(robot1, 30, 380, 30 + 10, 380 + 10)
    robotcanvas.update()
    while robot_on:
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
        print(refresh_speed)
        time.sleep(refresh_speed)


startButton.config(command=move_object)


root.mainloop()

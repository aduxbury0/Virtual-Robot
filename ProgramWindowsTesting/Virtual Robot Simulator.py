from tkinter import * # Imports Tkinter. - SHENIECE
import time # Imports time so that delays can be used within the program.- SHENIECE
##import winsound # Using Windows API, winsound allows audio to be imported or created.- SHENIECE
import ctypes #Allows message boxes to be used within the program. - SHENIECE
import turtle 

root = Tk() # Assigns the variable 'root' to Tkinter. - SHENIECE

# Opens the application in full screen mode - SHENIECE
fullScreen = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (fullScreen))
root.configure(bg = "black")

# The Exit function closes the program when called.- SHENIECE
def Exit():
    root.destroy()

# The Refresh function initalises the mazes on each page so that previous data is not stored from previous users. Thus, this will prevent the maze pages from
# recursion. - SHENIECE
def Refresh():
    easyP.destroy()
    intermediateP.destroy()
    hardP.destroy()
    selectDiff.pack()
    easyP.__init__()
    intermediateP.__init__()
    hardP.__init__()
    
# The Launch function open the start page containing the start button. - SHENIECE
def Launch():
    startP.pack()
    spTitle = Label(startP, text = "Virtual Robot\nSimulator!", bg = "black", fg = "snow", font = ("Bauhaus 93", 86), pady = 100) # Page title - SHENIECE
    spTitle.pack()
    startB = Button(startP, text = "Start", bg = "black", fg = "snow", font = ("Bauhaus 93", 50), command = Difficulty) # Start button - SHENIECE
    startB.pack(side = LEFT, padx = 300)

# The Difficulty function opens the 'Please Select A Maze' page, however since we wanted the layout to appear as a page rather than a seperate tk window, I used
# .pack() to lift the desired page and .pack_forget() to ensure that the remaining pages were not raised. Furthermore, I place the home button and exit button
# within this function so that it will appear on this page as well as on each maze page, so that I do not have to write the same code multiple times. - SHENIECE
def Difficulty():
    selectDiff.pack()
    homeB = Button(root, text = "Home", bg = "black", fg = "snow", font = ("Bauhaus 93", 20), command = Refresh) # Home button - SHENIECE
    homeB.place(relx = 1, x = -2, y = 2, anchor = NE)# Positions the Home button on the top right hand corner of the page - SHENIECE
    exitB = Button(root, text = "Exit", bg = "black", fg = "snow", font = ("Bauhaus 93", 20), command = Exit ) # Exit button - SHENIECE
    exitB.place(anchor = NW) # Positions the exit button on the top left hand corner of the page - SHENIECE
    startP.pack_forget()
    easyP.pack_forget()
    intermediateP.pack_forget()
    hardP.pack_forget()
    
  
# The Easy function 'lifts' the easy page and 'forgets' the 'Please Select A Maze (selectDiff)' page. - SHENIECE
def Easy():
    selectDiff.pack_forget()
    easyP.pack()
    easyP.configure(bg ="black")
    eTitle = Label(easyP, text = "Easy Maze", bg = "black", fg = "snow", font = ("Bauhaus 93", 30))# Page title - SHENIECE
    eTitle.pack()
# Beginning of Alex's Code
    robotDistance = 300000
    robot_speed_variable = StringVar()

    # This is the left hand side canvas for the robot to move on
    robotcanvas = Canvas(easyP, width=500, height=400, bg="white")
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
    controlFrame = Frame(easyP, width=300, height=400, bg="gray90", pady="10")
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


def set_speed():
    robot_speed = robot_speed_variable.get
    print(robot_speed)
    if robot_speed == str("1"):
        refresh_speed = int(float(0.45))
    elif robot_speed == str("2"):
        refresh_speed = int(float(0.4))
    elif robot_speed == str("3"):
        refresh_speed = int(float(0.35))
    elif robot_speed == str("4"):
        refresh_speed = int(float(0.3))
    elif robot_speed == str("5"):
        refresh_speed = int(float(0.25))
    elif robot_speed == str("6"):
        refresh_speed = int(float(0.2))
    elif robot_speed == str("7"):
        refresh_speed = int(float(0.15))
    elif robot_speed == str("8"):
        refresh_speed = int(float(0.1))
    elif robot_speed == str("9"):
        refresh_speed = int(float(0.05))
    else:
        refresh_speed = int(float(0.01))
    return refresh_speed


def stop_object():
    robot_on = False
    return robot_on

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
    refresh_speed = int(float(robot_speed_variable.get()))
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
    
# End of Alex's code

# The Intermediate function also 'lifts' the intermediate page and 'forgets' the 'Please Select A Maze (selectDiff)' page. - SHENIECE
def Intermediate():
    selectDiff.pack_forget()
    intermediateP.pack()
    intermediateP.configure(bg = "black")
    iTitle = Label(intermediateP, text = "Intermediate Maze", bg = "black", fg = "snow", font = ("Bauhaus 93", 30)) #Page title - SHENIECE
    iTitle.pack()

# Beginning of Rafael's code
    canvas = Canvas(intermediateP, width=500, height=500, bg='black')
    canvas.pack()

    #velocity

    vx = 5.0 
    vy = 5.0 

    #Boundries

    up=50
    right=470

    #Maze creation 
    line1=canvas.create_rectangle(30,50,70,520,fill='white',outline='white')
    line2=canvas.create_line(30,50,460,50,width=40,fill='white')
    line3=canvas.create_line(460,30,460,470,width=40,fill='white')
    line4=canvas.create_rectangle(200,430,478,470,fill='white',outline='white')
    line5=canvas.create_rectangle(180,470,220,300,fill='white',outline='white')
    line6=canvas.create_rectangle(200,300,400,340,fill='white',outline='white')
    line7=canvas.create_rectangle(200,300,400,340,fill='white',outline='white')
    line8=canvas.create_rectangle(380,340,420,140,fill='white',outline='white')
    line9=canvas.create_rectangle(100,120,420,160,fill='white',outline='white')
    line10=canvas.create_rectangle(100,120,140,520,fill='white',outline='white')
    finish=canvas.create_rectangle(100,470,140,520,fill='red')
    #robot
    robot=canvas.create_rectangle(40,480,60,500,fill="lightblue",outline="brown",width=2)


    #invisible boundire
    while True:
        x1,y1,x2,y2=canvas.coords(robot)
    #first move
        vy=-2
        vx=0
#conrinue trough the maze changing the direction by the boundarie
#second move
        if y1<up:
            vx=5.0
            vy=0.0
#third move
        if x2>=right:
            vx=0.0
            vy=5.0
#chnage the directions by the coords of the "lines"(rectangels)
#4th move
        if x1>=200 and y1>=430 and x2<=470 and y2<=470:
            vx=-5
            vy=0
#5th move
        if x1>=180 and y1>=340 and x1<=220 and y2<=470 and x2<=180 and x2<=220:
            vx=5
            vy=0
#6th move
        if x1>=180 and y1>=300 and x2<=400 and y2<=340:
            vx=5
            vy=0
#I figur it out that the 7th and 5th move are not necesary so i jump to 8
#8th move
        if x1>=100 and y1>=120 and x2<=420 and y2<=160 and x1<=420:
            vx=-5
            vy=0
#9th moeve
        if x1>=100 and y1>=120 and x2<=140 and y2<=500 and x1<=130:
            vx=0
            vy=5
#hit the finish line
        if x1>=100 and y1>=480 and x2<=140 and y2<=520 and x1<=130:
            vx=0
            vy=0
###This enables a series of beeps to be outputted when the robOt reaches the finish (red square); the beeps are then followed by a message box.- SHENIECE
##            winsound.Beep(740,150)
##            winsound.Beep(784,150)
##            winsound.Beep(784,150)
##            winsound.Beep(784,150)
##            winsound.Beep(370,150)
##            winsound.Beep(392,130)
##            time.sleep(3)# To avoid the message box from appearing before the audio output has finished, I used a 3 second delay. - SHENIECE
##            ctypes.windll.user32.MessageBoxW(0,"The Robot has managed to find its way around the Intermediate Maze!", "CONGRATULATIONS!",0)#The code below is used
##            #to bring up the message box after the audio output. - SHENIECE
##            time.sleep(2)
            
        canvas.coords(robot,x1+vx,y1+vy,x2+vx,y2+vy)
        canvas.update()
        time.sleep(0.01)
        
# End of Rafael's code   

# Just like the Easy and Intermediate pages, the Hard function 'lifts' the hard page and 'forgets' the 'Please Select A Maze (selectDiff)' page. - SHENIECE      
def Hard():
    selectDiff.pack_forget()
    hardP.pack()
    hardP.configure(bg = "black") # Makes the frame black - SHENIECE
    hTitle = Label(hardP, text = "Hard Maze", bg = "black", fg = "snow", font = ("Bauhaus 93", 30)) # Page title - SHENIECE
    hTitle.pack()
    
# Beginning of Amadou's code
    canvas = Canvas(hardP, width=500, height=500, bg='black')
    canvas.pack(padx=10,pady=10)
    #Draw lines in the arena
    canvas.create_line(0,50,450,50,fill="white",width=10)
    canvas.create_line(500,100,50,100,fill="white",width=10)
    canvas.create_line(50,100,50,450,fill="white",width=10)
    canvas.create_line(50,450,450,450,fill="white",width=10)
    canvas.create_line(500,400,100,400,fill="white",width=10)
    canvas.create_line(500,0,500,100,fill="white",width=10)
    canvas.create_line(0,500,500,500,fill="white",width=10)
    canvas.create_line(50,350,450,350,fill="white",width=10)
    canvas.create_line(100,300,500,300,fill="white",width=10)
    canvas.create_line(50,250,450,250,fill="white",width=10)
    canvas.create_line(100,200,500,200,fill="white",width=10)
    canvas.create_line(100,150,100,200,fill="white",width=10)
    canvas.create_line(100,150,500,150,fill="white",width=10)
    canvas.create_line(500,150,500,500,fill="white",width=10)
    canvas.create_line(550,0,550,550,fill="white",width=10)
    canvas.create_line(500,550,0,550,fill="white",width=10)
    # The velocity, or distance moved per time step
    vx = 10.0 # x velocity
    vy = 5.0 # y velocity
    # Boundaries
    x_min = 0.0
    y_min = 0.0
    x_max = 500.0
    y_max = 500.0

    id1=canvas.create_rectangle(3,7,3+10,7+10, fill = "white")
    # Move robot for 500 timesteps
    for t in range(1, 1000):
        x1,y1,x2,y2=canvas.coords(id1)
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
        canvas.coords(id1,x1+vx,y1+vy,x2+vx,y2+vy)
        canvas.update()
    # Pause for 0.1 seconds, then delete the image
        time.sleep(0.1)
        
# End of Amadou's code  
    
# First page - SHENIECE
startP = Frame(root)
startP.configure(bg = "black")

# Second page - SHENIECE
selectDiff = Frame(root)
selectDiff.configure(bg = "black")
sdTitle = Label(selectDiff, text = "Please Select A Maze:", bg = "black", fg = "snow", font = ("Bauhaus 93", 75), padx = 45, pady = 65)
sdTitle.pack()

easyB = Button(selectDiff, text = "Easy \nMaze", bg = "black", fg = "snow", font = ("Bauhaus 93", 40), command = Easy)
easyB.pack(side = LEFT, pady = 100)

intermediateB = Button(selectDiff, text = "Intermediate \nMaze", bg = "black", fg = "snow", font = ("Bauhaus 93", 40), command = Intermediate)
intermediateB.pack(side = LEFT, padx = 200, pady = 100)

hardB = Button(selectDiff, text = "Hard \nMaze", bg = "black", fg = "snow", font = ("Bauhaus 93", 40), command = Hard)
hardB.pack(side = RIGHT, pady = 100)

# Third page - SHENIECE
easyP = Frame(root)
canvas = Frame(root)

# Fourth page - SHENIECE
intermediateP = Frame(root)


# Fifth page - SHENIECE
hardP = Frame(root)

# First function that is called upon program launch - SHENIECE
Launch()

root.mainloop()
        



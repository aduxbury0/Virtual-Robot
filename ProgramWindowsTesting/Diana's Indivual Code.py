from tkinter import *
import time
global object1

# This is the main TK window
root = Tk()
root.resizable(width=False, height=False)


# This is the main frame within the Tk window, it sets the total size of the window
mainFrame = Frame(root, width=800, height=400)
mainFrame.pack()

# This is the left hand side canvas for the robot to move on
robotcanvas = Canvas(mainFrame, width=600, height=425, bg="grey")
#packs the canvas to the left of the main-frame.
robotcanvas.pack(side="left")

#This are the coordinates for each wall x1,y1,x2,y2.
easyWallObjectx=[0,50,0,170,100,120,170,450,120,500,500,525,430,600,570,600]
easyWallObjecty=[425,50,50,0,425,90,0,300,425,350,425,90,50,0,425,50]

#This are the walls for the maze for the robot to travel through.
wall1=robotcanvas.create_rectangle(easyWallObjectx[0],easyWallObjecty[0],easyWallObjectx[1],easyWallObjecty[1],width=2,fill="black")
wall2=robotcanvas.create_rectangle(easyWallObjectx[2],easyWallObjecty[2],easyWallObjectx[3],easyWallObjecty[3],width=2,fill="black")
wall3=robotcanvas.create_rectangle(easyWallObjectx[4],easyWallObjecty[4],easyWallObjectx[5],easyWallObjecty[5],width=2,fill="black")
wall4=robotcanvas.create_rectangle(easyWallObjectx[6],easyWallObjecty[6],easyWallObjectx[7],easyWallObjecty[7],fill="black")
wall5=robotcanvas.create_rectangle(easyWallObjectx[8],easyWallObjecty[8],easyWallObjectx[9],easyWallObjecty[9],width=2,fill="black")
wall6=robotcanvas.create_rectangle(easyWallObjectx[10],easyWallObjecty[10],easyWallObjectx[11],easyWallObjecty[11],width=2,fill="black")
wall7=robotcanvas.create_rectangle(easyWallObjectx[12],easyWallObjecty[12],easyWallObjectx[13],easyWallObjecty[13],width=2,fill="black")
wall8=robotcanvas.create_rectangle(easyWallObjectx[14],easyWallObjecty[14],easyWallObjectx[15],easyWallObjecty[15],width=2,fill="black")
#The finsih line 
finish_line = robotcanvas.create_rectangle(525, 400, 570, 600, fill="green", outline="")

#The intial width and height of the robotcanvas set for the object.
X_min=0.0
Y_min=0.0

X_max=600.0
Y_max=425.0

#robot1_moves is set to be true always so when the user clicks start it runs the entire code under it.
robot1_moves=True

#Initial drawing of the object block
object1=robotcanvas.create_rectangle(8,4,18,16, width=2, fill="blue")

#Initial drawing of the robot block
robot1=robotcanvas.create_rectangle(60,420,80,410,width=2,fill="red")

#The movement on the left of the object controlled by the user.
def Left(event):
    print ("Left")
    #stores the coordinates of the object movement.
    X1,Y1,X2,Y2=robotcanvas.coords(object1)
    #sets the direction of the object when going left.
    robotcanvas.coords(object1,X1-10,Y1,X2-10,Y2)
    
    #sets the boundaries in order for the object not to cross the height on the left hand side of the canvas.
    if X1< X_min:
       #set the object to move to the right if it tries crossing the height on the left hand side of the canvas.
       robotcanvas.coords(object1,X1+5,Y1,X2+5,Y2)
    #updates the robot canvas each time the user moves the object to the left. 
    robotcanvas.update()

    
#The movement on the right of the object controlled by the user.
def Right(event):
    print ("Right")
    #stores the coordinates of the object movement.
    X1,Y1,X2,Y2=robotcanvas.coords(object1)
    #sets the direction of the object when going right.
    robotcanvas.coords(object1,X1+10,Y1,X2+10,Y2)
    #sets the boundaries in order for the object not to cross the height on the right hand side of the canvas.
    if X2> X_max:
       #set the object to move to the left if it tries crossing the height on the right hand side of the canvas.
       robotcanvas.coords(object1,X1-5,Y1,X2-5,Y2)
    #updates the robot canvas each time the user moves the object to the right. 
    robotcanvas.update()

#The movement on the top of the object controlled by the user.
def Up(event):
    print ("Up")
    #stores the coordinates of the object movement.
    X1,Y1,X2,Y2=robotcanvas.coords(object1)
    #sets the direction of the object when going up.
    robotcanvas.coords(object1,X1,Y1-10,X2,Y2-10)
    #sets the boundaries in order for the object not to cross the width on the top of the canvas.
    if Y1< Y_min:
       #set the object to move downwards if it tries crossing the width at the top of the canvas.
       robotcanvas.coords(object1,X1,Y1+5,X2,Y2+5)
    #updates the robot canvas each time the user moves the object upwards. 
    robotcanvas.update()

#The movement on the bottom of the object controlled by the user.
def Down(event):
    print ("Down")
    #stores the coordinates of the object movement.
    X1,Y1,X2,Y2=robotcanvas.coords(object1)
    #sets the direction of the object when going down.
    robotcanvas.coords(object1,X1,Y1+10,X2,Y2+10)
    #sets the boundaries in order for the object not to cross the width on the bottom of the canvas.
    if Y2> Y_max:
       #set the object to move upwards if it tries crossing the width at the bottom of the canvas.
       robotcanvas.coords(object1,X1,Y1-5,X2,Y2-5)
    #updates the robot canvas each time the user moves the object downwards
    robotcanvas.update()



#When this function is called it will bind the variables left, right, up and down to the built in keys.
def move_object1():
    robotcanvas.bind('<Left>', Left)
    robotcanvas.bind('<Right>', Right)
    robotcanvas.bind('<Up>', Up)
    robotcanvas.bind('<Down>', Down)
#This groups the four keys to be accessible in the robotcanvas.
    robotcanvas.focus_set()
         
#When this function is called the computer controls the movement of the robot.
def move_robot1():
   
    #The intial width and height of the robotcanvas set for the robot .
    X_min=0.0
    Y_min=0.0

    X_max=600.0
    Y_max=425.0

    normalvelocity_X=0.0
    normalvelocity_Y=-6.0
    
    #Here is when the robot_moves is called and since it's always true it will run the enter code below it.
    while robot1_moves:
          #stores the coordinates of the robot movement
          x1,y1,x2,y2=robotcanvas.coords(robot1)
          #stores the coordinates of the object movement
          X1,Y1,X2,Y2=robotcanvas.coords(object1)

          #sets the boundaries in order for the robot not to cross the height on the left hand side of the canvas.
          if x2>= X_max:
             #sets the speed of the robot when going right to reverse left.
             normalvelocity_X=-20.0
             #sets the distance of the robot when going right to reverse left.
             robotcanvas.coords(object1,X1-10,Y1,X2-10,Y2)
             
          #sets the boundaries in order for the object not to cross the width on the top of the canvas.   
          if y1<=Y_min:
             #sets the speed of the robot when going up to reverse down.
             normalvelocity_Y=10.0
             #sets the distance of the robot when going up to reverse down.
             robotcanvas.coords(object1,X1,Y1+10,X2,Y2+10)

          #sets the boundaries in order for the object not to cross the height on the bottom of the canvas.   
          if y2>=Y_max:
             #sets the speed of the robot when going down to reverse up.
             normalvelocity_Y=-10.0
             #sets the distance of the robot when going down to reverse up.
             robotcanvas.coords(object1,X1,Y1-10,X2,Y2-10)
             
          #sets the boundaries in order for the object not to cross the height on the top of the canvas.    
          if x1<=X_min:
             #sets the speed of the robot when going left to reverse right.
             normalvelocity_X=20.0
             #sets the distance of the robot when going left to reverse right.
             robotcanvas.coords(object1,X1+10,Y1,X2+10,Y2)

#These are the boundaries of preventring the robot from avoid touching the walls of the arena and navigating within the maze.
#Also adding speed and direction of how to navigate around the maze.
             
#x2 of wall1
          if x1<=easyWallObjectx[1] :
             normalvelocity_X=10.0
             normalvelocity_Y=0.0
             robotcanvas.coords(robot1,x1+5,y1,x2+5,y2)
#x1 of wall3
          if x2>=easyWallObjectx[4]  and y1<easyWallObjecty[4]  and y1>=easyWallObjecty[5]:
             normalvelocity_X=-10.0
             normalvelocity_Y=0.0
             robotcanvas.coords(robot1,x1-5,y1,x2-5,y2)

#y2 of wall2 going down
          if y1<=(easyWallObjecty[3]+50) and x1<=easyWallObjectx[1]:
             normalvelocity_Y=10.0
             normalvelocity_X=0.0  
             robotcanvas.coords(robot1,x1,y1-5,x2,y2-5)
#y2 of wall2
          if y1<=(easyWallObjecty[2]+20):
             normalvelocity_Y=10.0
             normalvelocity_X=0.0  
             robotcanvas.coords(robot1,x1,y1+5,x2,y2+5)
             normalvelocity_X=10.0
             normalvelocity_Y=0.0
             robotcanvas.coords(robot1,x1+5,y1,x2+5,y2)
             
#y2 of wall2 preventing robot from leaving the walls            
          if y1<=easyWallObjecty[2] and x1>=easyWallObjectx[1]:
             normalvelocity_Y=10.0
             normalvelocity_X=0.0  
             robotcanvas.coords(robot1,x1,y1+5,x2,y2+5)
             
#x1 of wall4
          if x2>=(easyWallObjectx[6]-20) :
             normalvelocity_Y=10.0
             normalvelocity_X=0.0
             robotcanvas.coords(robot1,x1,y1+5,x2,y2+5)
             
#x2 of wall3
          if x1<=easyWallObjectx[5] and x1>=easyWallObjectx[4]:
             normalvelocity_Y=0.0
             normalvelocity_X=10.0
             robotcanvas.coords(robot1,x1-5,y1,x2-5,y2)
        
#y1 of wall5
          if y2>=(easyWallObjecty[8]-110) and x2>=(easyWallObjectx[6]-10):
             normalvelocity_X=10.0
             normalvelocity_Y=0.0
             robotcanvas.coords(robot1,x1+5,y1,x2+5,y2)
#x2 of wall3
          if y2<=(easyWallObjecty[8]) and x1>=easyWallObjectx[5] and y1>=(easyWallObjecty[7]+20):
             normalvelocity_X=10.0
             normalvelocity_Y=0.0
             robotcanvas.coords(robot1,x1+5,y1,x2+5,y2)
             
#y2 of wall2 preventing robot from leaving the walls.
          if y1<=easyWallObjecty[2] and x1>=easyWallObjectx[1]:
             normalvelocity_Y=10.0
             normalvelocity_X=0.0  
             robotcanvas.coords(robot1,x1,y1+5,x2,y2+5)
             normalvelocity_X=10.0
             normalvelocity_Y=0.0
             robotcanvas.coords(robot1,x1+5,y1,x2+5,y2)
#y1 of wall6
          if x2>=(easyWallObjectx[10]-20):
             normalvelocity_X=0.0
             normalvelocity_Y=-10.0
             robotcanvas.coords(robot1,x1,y1-5,x2,y2-5)
             
#x2 of wall4
          if x1>=easyWallObjectx[7]:
             normalvelocity_X=10.0
             normalvelocity_Y=0.0
             robotcanvas.coords(robot1,x1+5,y1,x2+5,y2)
             
#x2 of wall6
          if x2>=easyWallObjectx[10]:
             normalvelocity_X=-10.0
             normalvelocity_Y=0.0
             robotcanvas.coords(robot1,x1-5,y1,x2-5,y2)
             
#y2 of wall7 going up
          if y1>= easyWallObjecty[13] and x2>=(easyWallObjectx[10]-25):
             normalvelocity_Y=-10.0
             normalvelocity_X=0.0
             robotcanvas.coords(robot1,x1,y1-5,x2,y2-5)
             
#y1 of wall7 and x2 of wall4 going right 
          if y1<=(easyWallObjecty[12]+15) and x1>=easyWallObjectx[7]:
             normalvelocity_X=10.0
             normalvelocity_Y=0.0
             robotcanvas.coords(robot1,x1+5,y1,x2+5,y2)
             
#y2 of wall7 going back down then right
          if y1<=(easyWallObjecty[13]+50) and x1>=easyWallObjectx[7]:
              normalvelocity_Y=10.0
              normalvelocity_X=0.0  
              robotcanvas.coords(robot1,x1,y1-5,x2,y2-5)
              
#x1 of wall8 going
          if x2>=easyWallObjectx[14]:
             normalvelocity_X=-10.0
             normalvelocity_Y=0.0
             robotcanvas.coords(robot1,x1-5,y1,x2-5,y2)
             
#x1 of wall8 to go down
          if x2>=(easyWallObjectx[14]-10):
             normalvelocity_Y=10.0
             normalvelocity_X=0.0 
             robotcanvas.coords(robot1,x1,y1+5,x2,y2+5)
             
#x2 of wall6
          if x1<=easyWallObjectx[11] and x2>=easyWallObjectx[14]:
             normalvelocity_X=10.0
             normalvelocity_Y=0.0
             robotcanvas.coords(robot1,x1+5,y1,x2+5,y2)
             
#x1 of wall8
          if x2>=easyWallObjectx[14] and x1<=easyWallObjectx[11]:
             normalvelocity_X=-10.0
             normalvelocity_Y=0.0
             robotcanvas.coords(robot1,x1-5,y1,x2-5,y2)
             
#y1 of wall3
          if y2<=easyWallObjecty[4] and y1<=(easyWallObjecty[3]):
             normalvelocity_Y=-10.0
             normalvelocity_X=0.0  
             robotcanvas.coords(robot1,x1,y1-5,x2,y2-5)
#y2 of wall2             
          if y1<=easyWallObjecty[2]:
             normalvelocity_Y=0.0
             normalvelocity_X=10.0
             robotcanvas.coords(robot1,x1+5,y1,x2+5,y2)

##x1 of wall4
          if x2>=easyWallObjectx[6] and y2<=easyWallObjecty[7] and x1>=easyWallObjectx[7] and y1<=easyWallObjecty[2] and x1>=easyWallObjectx[1]:
             normalvelocity_Y=0.0
             normalvelocity_X=-10.0
             robotcanvas.coords(robot1,x1-5,y1,x2-5,y2)
             normalvelocity_Y=10.0
             normalvelocity_X=0.0
             
#y2 of wall 4            
          if y1<=(easyWallObjecty[7]) and x1>=easyWallObjectx[5] and y2<=easyWallObjecty[7] and y1<=easyWallObjecty[2] and x1>=easyWallObjectx[1]:
             normalvelocity_Y=0.0
             normalvelocity_X=10.0
             robotcanvas.coords(robot1,x1+5,y1,x2+5,y2)


#This test the IO of the robot detecting the object 10 distance away and increasing its speed it's travelling at.           
#when object1 is on the left hand side of robot1 and its height to get a close proximity. 
          if (X2+10)>=x1 and (Y2+10)>=y1:
             if normalvelocity_Y==-10.0:
                print("object1 on the left ,speed up going up2")
                normalvelocity_Y=-20.0
             elif normalvelocity_Y==-6.0:
                  print("object1 on the left, speed up going up1")
                  normalvelocity_Y=-10.0
             elif normalvelocity_Y==10.0:
                  print("object1 on the left, speed up going down")
                  normalvelocity_Y=20.0
             elif normalvelocity_X==-10.0:
                  print("object1 on the left, speed up going left")
                  normalvelocity_X=-20.0
             elif normalvelocity_X==10.0:
                  print("object1 on the left, speed up going right")
                  normalvelocity_X=20.0
#when object1 is on the Right hand side of robot1 and its height to get a close proximity. 
          elif (X1+10)>=x2 and (Y2+10)>=y1:
               if normalvelocity_Y==-10.0:
                  print("object1 on the right, speed up going up2")
                  normalvelocity_Y=-20.0
               elif normalvelocity_Y==-6.0:
                    print("object1 on the right, speed up going up1")
                    normalvelocity_Y=-10.0
               elif normalvelocity_Y==10.0:
                    print("object1 on the right, speed up going down")
                    normalvelocity_Y=20.0
               elif normalvelocity_X==-10.0:
                    print("object1 on the right, speed up going left")
                    normalvelocity_X=-20.0
               elif normalvelocity_X==10.0:
                    print("object1 on the right, speed up going right")
                    normalvelocity_X=20.0



             
#At the finsh line it restarts
          if y2>=Y_max:
              print("Finished")
              normalvelocity_Y=100.0
              normalvelocity_X=-100.0
              robotcanvas.coords(robot1,60,420,80,410)
#Stops the loop as soon as its reached the finish line the user has to press start button to to run through the while loop again.
              break




          #Sets the directioan and the speed of how the robot should navigate depending on the condditions above it.    
          robotcanvas.coords(robot1,x1+normalvelocity_X,y1+normalvelocity_Y,x2+normalvelocity_X,y2+normalvelocity_Y)
          #updates the robot canvas each time the robot direction and speed as been set.
          robotcanvas.update()
          #slows down the robot so the user can see the movement.
          time.sleep(0.1)
          

        

# This is half the right hand side of the control inputs, containing the start/throw object button.
ButtonFrame = Frame(mainFrame, width=300, height=200, bg="gray90",bd="5")
ButtonFrame.pack_propagate(0)
ButtonFrame.pack(side="right")

#This designs the Start button, the command for the button when pressed is to run move_robot1 function.
startButton = Button(ButtonFrame, text="Start",padx="10", pady="5",command=move_robot1)
#This is set on where to place the Start button on the Button Frame. 
startButton.grid(row="0", column="0", pady="15")       

#This designs the Throw Object button, the command for the button when pressed is to run move_object1 function.
throwObject = Button(ButtonFrame, text="Throw Object",padx="10", pady="5",command=move_object1)
#This is set on where to place the throw button on the Button Frame. 
throwObject.grid(row="1", column="0", pady="15")

#This is to keep the tk window opemned on a loop for the user to see whats running on the code.
root.mainloop()


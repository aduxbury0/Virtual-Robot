from tkinter import *
import time
window = Tk()
#creating the window
canvas = Canvas(window, width=500, height=500, bg='black')
canvas.pack()

#velocity

vx = 5.0 
vy = 5.0 

#Boundries

up=50
right=470

#Maze creation
#it is consited by rectangels and lines .
#Why there are more rectangels than lines ?
#It is more convinient for the robot to move by the coordonates of the rectangles , then the boundaries of the lines

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

#The movement of the robot

while True:
    x1,y1,x2,y2=canvas.coords(robot)
#first move
    vy=-2
    vx=0
#continue trough the maze changing the direction by the boundarie
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
    
    #cavas coords and canvas update will make your robots coordonates to change and to update every time it will make a move
    canvas.coords(robot,x1+vx,y1+vy,x2+vx,y2+vy)
    canvas.update()
    time.sleep(0.01)
    # time sleep is represented by the time which is used by the robot to make anathore move
    # if you change the time with a lower value then the one setted with a bigger one, the robot will move faster
    # vice versa to make the robot slowlier
                   
window.mainloop()


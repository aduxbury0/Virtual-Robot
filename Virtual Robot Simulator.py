from tkinter import *
import time

root = Tk()
root.geometry("800x400")
root.title("Virtual Robot Simulator")
root.configure(bg = "black")


def Launch():
    startP.pack()
    spTitle = Label(startP, text = "Virtual Robot\nSimulator!", bg = "black", fg = "snow", font = ("Bauhaus 93", 86), pady = 100)
    spTitle.pack()
    startB = Button(startP, text = "Start", bg = "black", fg = "snow", font = ("Bauhaus 93", 50), command = Difficulty)
    startB.pack(side = LEFT, padx = 300)


def Difficulty():
    selectDiff.pack()
    homeB = Button(root, text = "Home", bg = "black", fg = "snow", font = ("Bauhaus 93", 20), command = Difficulty)
    homeB.place(relx = 1, x = -2, y = 2, anchor = NE)
    startP.pack_forget()
    easyP.pack_forget()
    intermediateP.pack_forget()
    hardP.pack_forget()
    

def Easy():
    selectDiff.pack_forget()
    easyP.pack()
    eTitle = Label(easyP, text = "Easy Maze", bg = "black", fg = "snow", font = ("Bauhaus 93", 30))
    eTitle.pack(side = TOP)
   
    
def Intermediate():
    selectDiff.pack_forget()
    iTitle = Label(intermediateP, text = "Intermediate Maze", bg = "black", fg = "snow", font = ("Bauhaus 93", 30))
    iTitle.pack()
    intermediateP.pack()
  

def Hard():
    selectDiff.pack_forget()
    hTitle = Label(hardP, text = "Hard Maze", bg = "black", fg = "snow", font = ("Bauhaus 93", 30))
    hTitle.pack()
    hardP.pack()

# first frame
startP = Frame(root)
startP.configure(bg = "black")

# second frame - without selectDiff.pack()
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

# third frame - without easyP.pack()
easyP = Frame(root)



# fourth frame
intermediateP = Frame(root)

# fifth frame
hardP = Frame(root)

# show first frame
Launch()



root.mainloop()
        



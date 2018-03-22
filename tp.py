# This is written by Wanling Ding (wanlingd).

######################term project######################

from tkinter import *
import math

class Scripts(object):

    def __init__(self,x0,y0,x1,y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def clickWithin(self,other): # to detect mouse events
        return self.x0<=other.x<=self.x1 and self.y0<=other.y<=self.y1

    def dropIn(self,other): # to detect if anothe object is inside
        return self.x0<=other.x0 and self.x1>=other.x0+other.length and\
        self.y0<=other.y0 and self.y1>=other.y0+other.height

class DisplayBoard(Scripts):

    def __init__(self,x0,y0,x1,y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="white")

    def dropIn(self,other):
        return self.x0<=other.cx-other.r and self.x1>=other.cx+other.r and\
        self.y0<=other.cy-other.r and self.y1>=other.cy+other.r


class ActionBoard(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="light yellow")
        canvas.create_text(x0+(x1-x0)/2,y0+20,text="Your code",font="Chalkboard 20 italic")
        canvas.create_text(x0+(x1-x0)/2,y0+40,text="(Note that your code must be in sequence)",
                            font="Chalkboard")

    def isInBoard(self,other):
        return self.x0<=other.x0 and self.x1>=other.x0+other.length and\
        self.y0<=other.y0 and self.y1>=other.y0+other.height

    def clickWithin(self,other):
        return self.x0<=other.x<=self.x1 and self.y0<=other.y<=self.y1

class ToolBoard(ActionBoard):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="white")
        cx = x0+(x1-x0)/2
        canvas.create_text(cx,y0+40,text="Choose a color",font="Chalkboard 18")
        canvas.create_text(cx,y0+210,text="Choose a shape",font="Chalkboard 20")
        canvas.create_text(cx,y0+380,text="Use mouse to draw",font="Chalkboard 20")

class DisplayButton(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="light green")
        canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,text="Run",font="ComicSansMS")

class ClearButton(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="light blue")
        canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,text="Clear",font="ComicSansMS")

class UndoButton(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="pink")
        canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,text="Undo",font="ComicSansMS")

class SampleButton(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="orange")
        canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,text="Sample",font="ComicSansMS")

    def drawCode(self,canvas):
        canvas.create_text(950,225,text="repeat 2 times",anchor=W,font="Palatino 14 bold")
        canvas.create_text(950,245,text="turn right 90",anchor=W,font="Palatino 14")
        canvas.create_text(950,265,text="color red",anchor=W,font="Palatino 14",fill="red")
        canvas.create_text(950,285,text="move 200",anchor=W,font="Palatino 14")
        canvas.create_text(950,305,text="turn left 60",anchor=W,font="Palatino 14")
        canvas.create_text(950,325,text="color blue",anchor=W,font="Palatino 14",fill="blue")
        canvas.create_text(950,345,text="move 100",anchor=W,font="Palatino 14")
        canvas.create_text(950,365,text="end repeat",anchor=W,font="Palatino 14 bold")

class BackToCodeButton(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="orange")
        canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,text="Back",font="ComicSansMS")

class BackButton(object):

    def __init__(self,x0,y0,image):
        self.x0 = x0
        self.y0 = y0
        self.image = image

    def draw(self,canvas):
        x0,y0=self.x0,self.y0
        canvas.create_image(x0,y0,image=self.image)
        # canvas.create_rectangle(20,20,110,100)
        canvas.create_text(x0-20,y0,text="Back",font="ComicSansMS 18")

    def clickWithin(self,other):
        return 20<=other.x<=110 and 20<=other.y<=100

class Motion(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="pink")
        canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,
                           text="Motion",font="Chalkboard 20 italic")


class Move(Scripts):
    
    def __init__(self,x0,y0,length,height,input=""):
        self.x0,self.y0,self.length,self.height,self.input=\
        x0,y0,length,height,input

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,
                                fill="purple",outline="black")
        canvas.create_text(x0,y0,text="move            steps",font="Futura")
        canvas.create_rectangle(x0-15,y0-15,x0+15,y0+15,fill="white",outline="black")

    def clickWithin(self,other):
        return self.x0-self.length/2<=other.x<=self.x0+self.length/2 and \
        self.y0-self.height/2<=other.y<=self.y0+self.height/2

    def doMove(self,other):
        other.x0 += self.input

class TurnLeft(Move):

    def __init__(self,x0,y0,length,height,input=""):
        super().__init__(x0,y0,length,height,input)

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,fill="purple",
            outline="black")
        canvas.create_text(x0,y0,text="turn left            degrees",font="Futura")
        canvas.create_rectangle(x0-15,y0-15,x0+15,y0+15,fill="white",outline="black")

class TurnRight(TurnLeft):

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,fill="purple",
            outline="black")
        canvas.create_text(x0,y0,text="turn right            degrees",font="Futura")
        canvas.create_rectangle(x0-15,y0-15,x0+15,y0+15,fill="white",outline="black")


class MotionBoard(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="pink")
        xc = x0+(x1-x0)/2
        start = 50
        canvas.create_text(xc,y0+start,text="Make your character move",font="Klee 18")
        canvas.create_text(xc,y0+start+25,text="(Enter a number between 0 and 450)",font="Klee 14")
        canvas.create_text(xc,y0+start+120,text="Make your character turn left",font="Klee 18")
        canvas.create_text(xc,y0+start+145,text="(Enter a number between 0 and 180)",font="Klee 14")
        canvas.create_text(xc,y0+start+240,text="Make your character turn right",font="Klee 18")
        canvas.create_text(xc,y0+start+265,text="(Enter a number between 0 and 180)",font="Klee 14")



class Control(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="light blue")
        canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,
                           text="Control",font="Chalkboard 20 italic")

class ControlBoard(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="light blue")
        xc = x0+(x1-x0)/2
        start = 70
        canvas.create_text(xc,y0+start,text="Repeat the motion",font="Klee 18")
        canvas.create_text(xc,y0+start+25,text="(Enter a number to start the repeat)",font="Klee 14")
        canvas.create_text(xc,y0+start+140,text="End the repeat",font="Klee 18")
        canvas.create_text(xc,y0+start+165,text="(Make sure to add it after repeating)",font="Klee 14")

class Repeat(Move):

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,fill="light grey",
            outline="black")
        canvas.create_text(x0,y0,text="repeat           times",font="Futura")
        canvas.create_rectangle(x0-15,y0-15,x0+15,y0+15,fill="white",outline="black")


class EndRepeat(Repeat):

    def __init__(self,x0,y0,length,height):
        self.x0,self.y0,self.length,self.height=x0,y0,length,height

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,fill="light grey",
            outline="black")
        canvas.create_text(x0,y0,text="end repeat",font="Futura")
        # canvas.create_rectangle(x0-15,y0-15,x0+15,y0+15,fill="white",outline="black")

class Pause(Repeat):

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,fill="light grey",
            outline="black")
        canvas.create_text(x0,y0,text="pause               seconds")
        canvas.create_rectangle(x0-15,y0-15,x0+15,y0+15,fill="white",outline="black")


class Color(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="light green")
        canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,
                           text="Color",font="Chalkboard 20 italic")

class ColorBoard(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="light green")
        xc = x0+(x1-x0)/2
        start = 30
        canvas.create_text(xc,y0+start,text="Choose a color for your line",font="Klee 18")
        canvas.create_text(xc,y0+start+260,text="Create your own color",font="Klee 18")
        canvas.create_text(xc,y0+start+290,text="(Format: r+number+g+number+b+number)",font="Klee 14")
        canvas.create_text(xc,y0+start+310,text="(Numbers must be between 0 and 255)",font="Klee 14")
        canvas.create_text(xc,y0+start+330,text="(e.g. r60g100b180)",font="Klee 14")

class Red(EndRepeat):

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,
            fill="red",outline="black")
        canvas.create_text(x0,y0,text="Red",font="Futura 14")

class Blue(Red):

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,
            fill="blue",outline="black")
        canvas.create_text(x0,y0,text="Blue",font="Futura 14")

class Green(Red):

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,
            fill="green",outline="black")
        canvas.create_text(x0,y0,text="Green",font="Futura 14")

class Yellow(Red):

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,
            fill="yellow",outline="black")
        canvas.create_text(x0,y0,text="Yellow",font="Futura 14")

class Pink(Red):

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,
            fill="pink",outline="black")
        canvas.create_text(x0,y0,text="Pink",font="Futura 14")

class Purple(Red):

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,
            fill="purple",outline="black")
        canvas.create_text(x0,y0,text="Purple",font="Futura 14")

class Black(Red):

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,
            fill="black",outline="black")
        canvas.create_text(x0,y0,text="Black",fill="white",font="Futura 14")

class NoneColor(Red):

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,
            fill=None,outline="black")
        canvas.create_text(x0,y0,text="None",font="Futura 14")

class White(Red):

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,
            fill="white",outline="black")
        canvas.create_text(x0,y0,text="White",font="Futura 14")


class MyColor(Red):

    def __init__(self,x0,y0,length,height,input=""):
        super().__init__(x0,y0,length,height)
        self.input = input

    def draw(self,canvas):
        x0,y0,length,height=self.x0,self.y0,self.length,self.height
        canvas.create_rectangle(x0-length/2,y0-height/2,x0+length/2,y0+height/2,
            fill="white",outline="black")
        canvas.create_text(x0,y0,text="My color",font="Futura 14")


class Character(object):

    def __init__(self,x0,y0,image):
        self.x0 = x0
        self.y0 = y0
        self.image = image

    def draw(self,canvas):
        x0,y0 = self.x0,self.y0
        canvas.create_image(x0,y0,image=self.image)


class EasyMode(Scripts):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="white")
        canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,
                           text="Easy",font="Chalkboard 20")
    def drawShape(self,canvas):
        canvas.create_line(80,270,380,270,width=5)
        canvas.create_line(80,270,80,570,width=5)
        canvas.create_line(380,570,80,570,width=5)
        canvas.create_line(380,270,380,570,width=5)
        canvas.create_text(250,630,text="Can you use the codes to redraw the shape?",font="Chalkboard 16")

class MediumMode(EasyMode):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="white")
        canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,
                           text="Medium",font="Chalkboard 20")
    def drawShape(self,canvas):
        canvas.create_line(80,270,380,270,width=5)
        canvas.create_line(380,270,380,345,width=5)
        canvas.create_line(380,345,80,345,width=5)
        canvas.create_line(80,345,80,420,width=5)
        canvas.create_line(80,420,380,420,width=5)
        canvas.create_line(380,420,380,495,width=5)
        canvas.create_line(380,495,80,495,width=5)
        canvas.create_line(80,495,80,570,width=5)
        canvas.create_text(250,630,text="Can you use the codes to redraw the shape?",font="Chalkboard 16")

class HardMode(EasyMode):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="white")
        canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,
                           text="Hard",font="Chalkboard 20")
    def drawShape(self,canvas):

        canvas.create_line(80,270,380,270,width=5) # length 300 --
        canvas.create_line(380,270,380,570,width=5) # length 300 |
        canvas.create_line(380,570,80,570,width=5) # length 300 --

        canvas.create_line(80,570,80,320,width=5) # length 250 |
        canvas.create_line(80,320,330,320,width=5) # length 250 --
        canvas.create_line(330,320,330,520,width=5) # length 200 |
        canvas.create_line(330,520,130,520,width=5) # length 200 --
        canvas.create_line(130,520,130,370,width=5) # length 150 |

        canvas.create_line(130,370,280,370,width=5) # length 150 --
        canvas.create_line(280,370,280,470,width=5) # length 100 |
        canvas.create_line(280,470,180,470,width=5) # length 100 --

        canvas.create_line(180,470,180,420,width=5) # length 50 |
        canvas.create_line(180,420,230,420,width=5) # length 50 |   

        canvas.create_text(250,630,text="Can you use the codes to redraw the shape?",font="Chalkboard 16")

class CreateMode(EasyMode):

    def draw(self,canvas):
        x0,y0,x1,y1=self.x0,self.y0,self.x1,self.y1
        canvas.create_rectangle(x0,y0,x1,y1,fill="white")
        canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,
                           text="Create",font="Chalkboard 20")
    def drawShape(self,canvas):
        canvas.create_text(180,620,text="Click on the screen to draw lines",font="Chalkboard 16")

class Circle(object):

    def __init__(self,cx,cy,r,color):
        self.cx,self.cy = cx,cy
        self.r = r
        self.color = color

    def draw(self,canvas):
        cx,cy = self.cx,self.cy
        r = self.r
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=self.color,outline='black',width=3)

    def clickWithin(self,other):
        cx,cy,r = self.cx,self.cy,self.r
        x0,x1,y0,y1 = cx-r,cx+r,cy-r,cy+r
        return x0<=other.x<=x1 and y0<=other.y<=y1

class Square(Circle):

    def draw(self,canvas):
        cx,cy = self.cx,self.cy
        r = self.r
        canvas.create_rectangle(cx-r,cy-r,cx+r,cy+r,fill=self.color,outline='black',width=3)

class Triangle(Circle):

    def draw(self,canvas):
        cx,cy = self.cx,self.cy
        r = self.r
        canvas.create_polygon(cx,cy-r,cx-math.cos(math.radians(30))*r,
                                cy+r*math.sin(math.radians(30)),
                                cx+math.cos(math.radians(30))*r,
                                cy+r*math.sin(math.radians(30)),
                                fill=self.color,outline='black',width=3)

class Pen(Circle):
    def draw(self,canvas):
        cx,cy = self.cx,self.cy
        r = self.r
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=self.color)


def init(data):

    data.mode = 'splashScreen'

    data.cloud = PhotoImage(file="cloud.gif")
    data.imageCloud = data.cloud.subsample(2,2)
    data.cloud1 = data.cloud.subsample(3,3)

    data.imagePalette = PhotoImage(file="palette.gif")
    data.palette = data.imagePalette.subsample(8,8)

    data.imageKitty = PhotoImage(file='kitty.gif')
    data.kitty1 = data.imageKitty.subsample(3,3)
    data.kitty2 = data.kitty1.zoom(2,2)
    data.kitty = data.imageKitty.subsample(4,4)
    data.isKitty = False
    
    data.imageSnoopy = PhotoImage(file='snoopy.gif')
    data.snoopy = data.imageSnoopy.subsample(3,3)
    data.isSnoopy = False

    data.imageSpongebob = PhotoImage(file='spongebob.gif')
    data.spongebob = data.imageSpongebob.subsample(3,3)
    data.isSpongebob = False

    data.imageSpiderman = PhotoImage(file='spiderman.gif')
    data.spiderman1 = data.imageSpiderman.subsample(3,3)
    data.spiderman = data.imageSpiderman.subsample(6,6)
    data.isSpiderman = False

    data.playBackground = PhotoImage(file="play.gif")
    data.splashBackground = PhotoImage(file="splash.gif")
    data.chooseBackground = PhotoImage(file="choose.gif")
    data.drawBackground = PhotoImage(file="draw.gif")
    data.helpBackground = PhotoImage(file="help.gif")

    data.DisplayBoard = DisplayBoard(30,200,480,650)

    data.ClearButtonCreate = ClearButton(410,610,470,640)
    data.UndoButtonCreate = UndoButton(340,610,400,640)
    

    data.Scripts = Scripts(500,250,825,650)
    data.ActionBoard = ActionBoard(845,160,1170,650)
    data.Character = Character(80,270,data.spongebob)
    data.oriX,data.oriY = data.Character.x0,data.Character.y0

    data.EasyMode = EasyMode(30,160,142.5,200)
    data.isEasyMode = True

    data.MediumMode = MediumMode(142.5,160,255,200)
    data.isMediumMode = False

    data.HardMode = HardMode(255,160,367.5,200)
    data.isHardMode = False

    data.CreateMode = CreateMode(367.5,160,480,200)
    data.isCreateMode = False

    data.Motion = Motion(500,160,500+325/3,210)
    data.Control = Control(500+325/3,160,500+325/3*2,210)
    data.Color = Color(500+325/3*2,160,825,210)

    data.MotionBoard = MotionBoard(500,210,825,650)
    data.isMotionBoard = True

    data.ControlBoard = ControlBoard(500,210,825,650)
    data.isControlBoard = False

    data.ColorBoard = ColorBoard(500,210,825,650)
    data.isColorBoard = False

    data.MotionStuff = []
    data.ControlStuff = []
    data.ColorStuff = []
    data.allMoves = []
    data.allCharPos = []

    length = 180
    height = 40

    data.Move = Move(662.5,330,length,height)
    data.MotionStuff.append(data.Move)

    data.Repeat = Repeat(662.5,350,length,height)
    data.ControlStuff.append(data.Repeat)

    
    data.TurnLeft = TurnLeft(662.5,450,length,height)
    data.MotionStuff.append(data.TurnLeft)

    data.EndRepeat = EndRepeat(662.5,490,length,height)
    data.ControlStuff.append(data.EndRepeat)


    data.TurnRight = TurnRight(662.5,570,length,height)
    data.MotionStuff.append(data.TurnRight)

    data.Red = Red(590,290,120,height)
    data.ColorStuff.append(data.Red)

    data.Blue = Blue(735,290,120,height)
    data.ColorStuff.append(data.Blue)

    data.Green = Green(590,345,120,height)
    data.ColorStuff.append(data.Green)

    data.Yellow = Yellow(735,345,120,height)
    data.ColorStuff.append(data.Yellow)

    data.Pink = Pink(590,400,120,height)
    data.ColorStuff.append(data.Pink)

    data.Purple = Purple(735,400,120,height)
    data.ColorStuff.append(data.Purple)

    data.Black = Black(590,455,120,height)
    data.ColorStuff.append(data.Black)

    data.NoneColor = NoneColor(735,455,120,height)
    data.ColorStuff.append(data.NoneColor)

    data.MyColor = MyColor(662.5,610,120,height)
    data.ColorStuff.append(data.MyColor)

    data.picBoard = DisplayBoard(80,180,550,650)
    data.ToolBoard = ToolBoard(600,180,1100,650)

    width = 120
    data.Red1 = Red(710,270,width,height)
    data.Blue1 = Blue(850,270,width,height)
    data.Green1 = Green(990,270,width,height)
    data.Yellow1 = Yellow(710,330,width,height)
    data.Black1 = Black(850,330,width,height)
    data.White1 = White(990,330,width,height)


    data.kittyColor = None
    data.spongebobColor = None
    data.snoopyColor = None
    data.spidermanColor = None

    data.DisplayButton = DisplayButton(1100,610,1160,640)
    data.isRun = False
    data.isDraw = False

    data.ClearButtonAction = ClearButton(1030,610,1090,640)
    data.UndoButtonAction = UndoButton(960,610,1020,640)
    data.SampleButton = SampleButton(890,610,950,640)
    data.isSample = False
    data.BackToCodeButton = BackToCodeButton(890,610,950,640)

    data.BackButton = BackButton(90,60,data.cloud1)

    data.ClearButtonDraw = ClearButton(500,610,540,640)

    data.drawShape = []

    data.Circle = Circle(710,470,50,None)
    data.newCircle = data.Circle

    data.Square = Square(850,470,50,None)
    data.newSquare = data.Square

    data.Triangle = Triangle(990,485,65,"white")
    data.newTriangle = data.Triangle

    data.imagePen = PhotoImage(file='pen.gif')
    data.pen = data.imagePen.subsample(6,6)

    data.drawColor = None

    data.onShape = {}
    data.movements = []

    data.isMove = False
    data.isTurnLeft = False
    data.isTurnRight = False
    data.isRepeat = False
    data.isEndRepeat = False

    data.isMyColor = False

    data.charPos = []
    data.charPos.append((data.Character.x0,data.Character.y0))
    data.degree = 0

    data.allPos = []
    data.myTime = 0

    data.drawLine = []
    data.createDraw = []
    data.createDraw.append((data.oriX,data.oriY))

    data.penPos = []
    data.isPen = False
    data.penDraw = []

    data.fileName = None
    data.imageFile = None


# adapted from http://www.cs.cmu.edu/~112/notes/notes-animations-examples.html#modeDemo

def mousePressed(event, data):
    if (data.mode == "splashScreen"): splashScreenMousePressed(event, data)
    elif (data.mode == "play"):   playMousePressed(event, data)
    elif (data.mode == "chooseImage"): chooseImageMousePressed(event, data)
    elif (data.mode == "draw"): drawMousePressed(event, data)
    elif (data.mode == "help"): helpMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "splashScreen"): splashScreenKeyPressed(event, data)
    elif (data.mode == "play"):   playKeyPressed(event, data)
    elif (data.mode == "chooseImage"):  chooseImageKeyPressed(event, data)
    elif (data.mode == "draw"):  drawKeyPressed(event, data)
    elif (data.mode == "help"):  helpKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "splashScreen"): splashScreenTimerFired(data)
    elif (data.mode == "play"):   playTimerFired(data)
    elif (data.mode == "chooseImage"):  chooseImageTimerFired(data)
    elif (data.mode == "draw"):  drawTimerFired(data)
    elif (data.mode == "help"):  helpTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "splashScreen"): splashScreenRedrawAll(canvas, data)
    elif (data.mode == "play"):   playRedrawAll(canvas, data)
    elif (data.mode == "chooseImage"):   chooseImageRedrawAll(canvas, data)
    elif (data.mode == "draw"):  drawRedrawAll(canvas, data)
    elif (data.mode == "help"):  helpRedrawAll(canvas, data)


#################### play mode ####################

def removeRepeat(motionList): # replace repeat with actions inside
    
    for i in range(len(motionList)-1,-1,-1):
        if "repeat times" in motionList[i][0]:
            times = int(motionList[i][1])
            for stuff in motionList[i:]:
                if "end" in stuff[0]:
                    stuff.extend("a")
                    j = motionList.index(stuff)
                    motionList = motionList[:i]+motionList[i+1:j]*times+motionList[j+1:]
                    break

    return motionList


def getAllPos(oriX,oriY,motionList): # get all the pos that char needs to go to

    degree = 0
    result = []
    result.append((oriX,oriY,"none"))

    for i in range(len(motionList)):
        # print(movements)

        if "left" in motionList[i][0]:
            if len(motionList[i][1])>0:
                degree += -int(motionList[i][1])
                # print(degree)

        elif "right" in motionList[i][0]:
            if len(motionList[i][1])>0:
                degree += int(motionList[i][1])

        elif "move" in motionList[i][0]:
            if len(motionList[i][1])>0:
                color = 0
                for action in motionList[:i][::-1]:

                    if action[0] == "my color":
                        color = makeColor(action[1])
                        break

                    elif action[0] == "color":
                        color = action[1]
                        break

                if color == 0:
                    color = "none"

                # print(color)

                distance = int(motionList[i][1])

                distanceX = distance*math.cos(math.radians(degree))
                distanceY = distance*math.sin(math.radians(degree))

                targetX = distanceX+oriX
                targetY = distanceY+oriY
                result.append((targetX,targetY,color))
                oriX,oriY = targetX,targetY

    return result


def allBetweenPos(posList): # get all intermediate pos
    result = []
    steps = 10
    for i in range(len(posList)-1):
        x0,y0,color0 = posList[i]
        x1,y1,color1 = posList[i+1]

        xsteps = (x1-x0)/steps
        ysteps = (y1-y0)/steps
        for i in range(steps+1):
            result.append((x0+xsteps*i,y0+ysteps*i,color1))

    return result


def isValidRGB(s): # check if the input rgb is valid
    if len(s)<=0:
        return False
    ri = s.find("r")
    gi = s.find("g")
    bi = s.find("b")

    if ri==-1 or gi==-1 or bi==-1:
        return False

    r = s[ri+1:gi]
    g = s[gi+1:bi]
    b = s[bi+1:]

    if len(r)<=0 or len(g)<=0 or len(b)<=0:
        return False

    red = int(r)
    green = int(g)
    blue = int(b)

    if red<0 or red>255 or green<0 or green>255 or blue<0 or blue>255:
        return False

    listOfLetters = ["acdefhijklmnopqstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]

    for c in s:
        if c in listOfLetters:
            return False

    return True

def isLegal(motionList): # check if the input code is valid

    repeatCount = 0
    endRepeatCount = 0

    for i in range(len(motionList)):

        if "move" in motionList[i][0] and len(motionList[i][1]) <= 0:
            return 'Error: Check your inputs after "move"!'

        elif "left" in motionList[i][0] and len(motionList[i][1]) <= 0:
            return 'Error: Check your inputs after "turn left"!'
        
        elif "right" in motionList[i][0] and len(motionList[i][1]) <= 0:
            return 'Error: Check your inputs after "turn right"!'

        elif "repeat times" in motionList[i][0] and len(motionList[i][1]) <= 0:
            return 'Error: Check your inputs after "repeat"!'

        elif "my color" in motionList[i][0] and not isValidRGB(motionList[i][1]):
            return 'Error: Check your color inputs!'

        if "repeat times" in motionList[i][0]:
            repeatCount += 1

        if "end repeat" in motionList[i][0]:
            endRepeatCount += 1

    if repeatCount != endRepeatCount:
        return 'Error: Check your loops!'

    else:
        return ""




# adapted from http://www.cs.cmu.edu/~112/notes/notes-graphics.html

def makeColor(s): # use the given rgb values to make color

    ri = s.find("r")
    gi = s.find("g")
    bi = s.find("b")
    r = int(s[ri+1:gi])
    g = int(s[gi+1:bi])
    b = int(s[bi+1:])
    return "#%02x%02x%02x" % (r,g,b)


def playMousePressed(event, data):

    if data.EasyMode.clickWithin(event):
        data.isEasyMode = True
        data.isMediumMode = False
        data.isHardMode = False
        data.isCreateMode = False
        data.Character.x0,data.Character.y0 = data.oriX,data.oriY
        data.drawLine = []
        data.isRun = False
        data.isDraw = False

    if data.MediumMode.clickWithin(event):
        data.isEasyMode = False
        data.isMediumMode = True
        data.isHardMode = False
        data.isCreateMode = False
        data.Character.x0,data.Character.y0 = data.oriX,data.oriY
        data.drawLine = []
        data.isRun = False
        data.isDraw = False

    if data.HardMode.clickWithin(event):
        data.isEasyMode = False
        data.isMediumMode = False
        data.isHardMode = True
        data.isCreateMode = False
        data.Character.x0,data.Character.y0 = data.oriX,data.oriY
        data.drawLine = []
        data.isRun = False
        data.isDraw = False

    if data.CreateMode.clickWithin(event):
        data.isEasyMode = False
        data.isMediumMode = False
        data.isHardMode = False
        data.isCreateMode = True
        data.Character.x0,data.Character.y0 = data.oriX,data.oriY
        data.drawLine = []
        data.isRun = False
        data.isDraw = False

    if data.isCreateMode:

        if data.ClearButtonCreate.clickWithin(event):
            data.createDraw = []
            data.createDraw.append((data.oriX,data.oriY))

        elif data.UndoButtonCreate.clickWithin(event) and len(data.createDraw)>0:
            data.createDraw.pop()

        elif data.DisplayBoard.clickWithin(event):
            data.createDraw.append((event.x,event.y))


    if data.Motion.clickWithin(event):
        data.isMotionBoard = True
        data.isControlBoard = False
        data.isColorBoard = False

    if data.Control.clickWithin(event):
        data.isControlBoard = True
        data.isMotionBoard = False
        data.isColorBoard = False

    if data.Color.clickWithin(event):
        data.isColorBoard = True
        data.isMotionBoard = False
        data.isControlBoard = False

    if data.BackButton.clickWithin(event):
        data.mode="splashScreen"
        data.isRun = False
        data.isDraw = False
        data.movements = []
        data.drawLine = []

    canvas = event.widget.canvas


    length = 130
    margin = 20
    height = 40

    step = 1

    if data.isMotionBoard:

        if data.Move.clickWithin(event):
            data.movements.append(["move  steps",data.Move.input])
            data.isMove = True
            data.isRun = False
            data.isDraw = False

        elif data.TurnLeft.clickWithin(event):
            data.movements.append(["turn left  degrees",data.TurnLeft.input])
            data.isTurnLeft = True
            data.isRun = False
            data.isDraw = False

        elif data.TurnRight.clickWithin(event):
            data.movements.append(["turn right  degrees",data.TurnRight.input])
            data.isTurnRight = True
            data.isRun = False
            data.isDraw = False


    if data.isControlBoard:

        if data.Repeat.clickWithin(event):
            data.movements.append(["repeat times",data.Repeat.input])
            data.isRepeat = True
            data.isRun = False
            data.isDraw = False

        elif data.EndRepeat.clickWithin(event):
            data.movements.append(["end repeat"])
            data.isEndRepeat = True
            data.isRun = False
            data.isDraw = False


    if data.isColorBoard:

        if data.Red.clickWithin(event):
            data.movements.append(["color","red"])
            data.isRun = False
            data.isDraw = False

        elif data.Blue.clickWithin(event):
            data.movements.append(["color","blue"])
            data.isRun = False
            data.isDraw = False

        elif data.Green.clickWithin(event):
            data.movements.append(["color","green"])
            data.isRun = False
            data.isDraw = False

        elif data.Yellow.clickWithin(event):
            data.movements.append(["color","yellow"])
            data.isRun = False
            data.isDraw = False

        elif data.Pink.clickWithin(event):
            data.movements.append(["color","pink"])
            data.isRun = False
            data.isDraw = False

        elif data.Purple.clickWithin(event):
            data.movements.append(["color","purple"])
            data.isRun = False
            data.isDraw = False

        elif data.Black.clickWithin(event):
            data.movements.append(["color","black"])
            data.isRun = False
            data.isDraw = False

        elif data.NoneColor.clickWithin(event):
            data.movements.append(["color","none"])
            data.isRun = False
            data.isDraw = False

        elif data.MyColor.clickWithin(event):
            data.movements.append(["my color",data.MyColor.input])
            data.isMyColor = True
            data.isRun = False
            data.isDraw = False


    if data.ClearButtonAction.clickWithin(event):
        data.movements = []
        data.isRun = False
        data.isDraw = False
        data.Character.x0,data.Character.y0 = data.oriX,data.oriY
        data.drawLine = []

    if data.UndoButtonAction.clickWithin(event):
        data.movements.pop()
        data.isRun = False
        data.isDraw = False
        data.drawLine = []

    if data.DisplayButton.clickWithin(event):
        data.isRun = True
        data.isDraw = True
        data.myTime = 0
        data.Character.x0,data.Character.y0 = data.oriX,data.oriY
        data.drawLine = []

    # else:
    #     data.isRun = False
    #     data.isDraw = False

    if not data.isRun:
        data.Character.x0,data.Character.y0=data.oriX,data.oriY

    if data.SampleButton.clickWithin(event):
        data.isSample = not data.isSample

    if isLegal(data.movements) == "":
        data.allMoves = removeRepeat(data.movements)
        data.charPos = getAllPos(data.oriX,data.oriY,data.allMoves)
        data.allPos = allBetweenPos(data.charPos)


def playKeyPressed(event, data):

    if data.isMove:
        if event.keysym.isdigit():
            for movements in data.movements[::-1]:
                if "move" in movements[0]:
                    movements[1] += event.keysym
                break

    if data.isTurnLeft:
        if event.keysym.isdigit():
            for movements in data.movements[::-1]:
                if "left" in movements[0]:
                    movements[1] += event.keysym
                break

    if data.isTurnRight:
        if event.keysym.isdigit():
            for movements in data.movements[::-1]:
                if "right" in movements[0]:
                    movements[1] += event.keysym
                break

    if data.isRepeat:
        if event.keysym.isdigit():
            for movements in data.movements[::-1]:
                if "repeat times" in movements[0]:
                    movements[1] += event.keysym
                break

    if data.isMyColor:
        if event.keysym.isalnum():
            for movements in data.movements[::-1]:
                if "my color" in movements[0]:
                    movements[1] += event.keysym
                break


def playTimerFired(data):

    if data.isRun:
        data.myTime += 1

        if isLegal(data.movements)=="":

            if data.myTime<len(data.allPos):
                data.Character.x0 = data.allPos[data.myTime][0]
                data.Character.y0 = data.allPos[data.myTime][1]

            if data.myTime == len(data.allPos):
                data.isRun = False


def playRedrawAll(canvas, data):

    canvas.create_image(data.width/2,data.height/2,image=data.playBackground)
    canvas.create_text(data.width/2,80,text="Let's learn to code!",font="Phosphate 60")

    data.DisplayBoard.draw(canvas)
    data.ActionBoard.draw(canvas)
    data.DisplayButton.draw(canvas)
    data.ClearButtonAction.draw(canvas)
    data.UndoButtonAction.draw(canvas)
    data.BackButton.draw(canvas)
    
    data.Motion.draw(canvas)
    data.Control.draw(canvas)
    data.Color.draw(canvas)
    data.EasyMode.draw(canvas)
    data.MediumMode.draw(canvas)
    data.HardMode.draw(canvas)
    data.CreateMode.draw(canvas)

    if not data.isSample:
        data.SampleButton.draw(canvas)
    else:
        data.SampleButton.drawCode(canvas)
        data.BackToCodeButton.draw(canvas)

    if data.isEasyMode:
        data.EasyMode.drawShape(canvas)

    if data.isMediumMode:
        data.MediumMode.drawShape(canvas)

    if data.isHardMode:
        data.HardMode.drawShape(canvas)

    if data.isCreateMode:
        data.CreateMode.drawShape(canvas)
        data.ClearButtonCreate.draw(canvas)
        data.UndoButtonCreate.draw(canvas)
        for i in range(len(data.createDraw)-1):
            x0,y0 = data.createDraw[i]
            x1,y1 = data.createDraw[i+1]
            canvas.create_line(x0,y0,x1,y1,width=5)

    for stuff in data.MotionStuff:
        if data.ActionBoard.isInBoard(stuff):
            stuff.draw(canvas)

    for stuff in data.ControlStuff:
        if data.ActionBoard.isInBoard(stuff):
            stuff.draw(canvas)

    if data.isMotionBoard:
        data.MotionBoard.draw(canvas)
        for stuff in data.MotionStuff:
            stuff.draw(canvas)

    if data.isControlBoard:
        data.ControlBoard.draw(canvas)
        for stuff in data.ControlStuff:
            stuff.draw(canvas)

    if data.isColorBoard:
        data.ColorBoard.draw(canvas)
        for stuff in data.ColorStuff:
            stuff.draw(canvas)
        canvas.create_image(760,600,image=data.palette)

    y = 225
    x = 950
    space = 20

    if not data.isSample:
        for movements in data.movements:

            if "move" in movements[0]:
                canvas.create_text(x,y,text="move %s steps"%movements[1],anchor=W,font="Palatino 14")
         
            elif "left" in movements[0]:
                canvas.create_text(x,y,text="turn left %s degrees"%movements[1],anchor=W,font="Palatino 14")
           
            elif "right" in movements[0]:
                canvas.create_text(x,y,text="turn right %s degrees"%movements[1],anchor=W,font="Palatino 14")
            
            elif "repeat times" in movements[0]:
                canvas.create_text(x,y,text="repeat %s times"%movements[1],anchor=W,font="Palatino 14 bold")
             
            elif "end repeat" in movements[0]:
                canvas.create_text(x,y,text="end repeat",anchor=W,font="Palatino 14 bold")
             
            elif "my color" in movements[0]:
                canvas.create_text(x,y,text="my color %s"%movements[1],anchor=W,fill="black",font="Palatino 14")
               
            elif "none" in movements[1]:
                canvas.create_text(x,y,text="color %s"%movements[1],anchor=W,fill="black",font="Palatino 14")
                
            elif "color" in movements[0]:
                canvas.create_text(x,y,text="color %s"%movements[1],anchor=W,fill=movements[1],font="Palatino 14")
            
            y += space

    if data.isRun:
        canvas.create_text(1007.5,590,text=isLegal(data.movements))

    if data.isDraw and isLegal(data.movements)=="":

        for i in range(len(data.allPos)-1):
            if data.myTime == i:
                x0,y0,color0 = data.allPos[i]
                x1,y1,color1 = data.allPos[i+1]
                data.drawLine.append([(x0,y0),(x1,y1),color0])

        for stuff in data.drawLine:
            if stuff[2] == "none":
                continue
            canvas.create_line(stuff[0],stuff[1],width=5,fill=stuff[2])



    data.Character.draw(canvas)



#################### choose mode #################### DONE


def chooseImageMousePressed(event,data):

    if data.BackButton.clickWithin(event):
        data.mode = "splashScreen"
        data.isKitty = False
        data.isSpongebob = False
        data.isSnoopy = False
        data.isSpiderman = False

    elif 200<=event.y<=420:

        if 140<=event.x<=300:
            data.Character.image = data.kitty
            data.isKitty = True
            data.isSpongebob = False
            data.isSnoopy = False
            data.isSpiderman = False

        elif 370<=event.x<=610:
            data.Character.image = data.spongebob
            data.isKitty = False
            data.isSpongebob = True
            data.isSnoopy = False
            data.isSpiderman = False

        elif 680<=event.x<=860:
            data.Character.image = data.snoopy
            data.isKitty = False
            data.isSpongebob = False
            data.isSnoopy = True
            data.isSpiderman = False

        elif 940<=event.x<=1080:
            data.Character.image = data.spiderman
            data.isKitty = False
            data.isSpongebob = False
            data.isSnoopy = False
            data.isSpiderman = True
            
    elif 490<=event.x<=640 and 490<=event.y<=610:
        data.mode="play"
        data.isKitty = False
        data.isSpongebob = False
        data.isSnoopy = False
        data.isSpiderman = False

def chooseImageKeyPressed(event,data):
    pass

def chooseImageTimerFired(data):
    pass

def chooseImageRedrawAll(canvas,data):
    canvas.create_image(data.width/2,data.height/2,image=data.chooseBackground)
    data.BackButton.draw(canvas)
    
    canvas.create_text(data.width/2,100,text="Choose your character!",font="Phosphate 60")
    canvas.create_image(data.width*0.18,data.height*0.45,image=data.kitty2)
    canvas.create_image(data.width*0.41,data.height*0.45,image=data.imageSpongebob)
    canvas.create_image(data.width*0.64,data.height*0.45,image=data.imageSnoopy)
    canvas.create_image(data.width*0.84,data.height*0.45,image=data.spiderman1)
    canvas.create_image(data.width/2,550,image=data.imageCloud)
    canvas.create_text(data.width/2-35,550,text="OK!",font="ComicSansMS 30 bold")

    r = 150

    if data.isKitty:
        canvas.create_oval(220-r,310-r,220+r,310+r,width=5,outline="blue")
    elif data.isSpongebob:
        canvas.create_oval(490-r,310-r,490+r,310+r,width=5,outline="blue")
    elif data.isSnoopy:
        canvas.create_oval(770-r,310-r,770+r,310+r,width=5,outline="blue")
    elif data.isSpiderman:
        canvas.create_oval(1010-r,310-r,1010+r,310+r,width=5,outline="blue")


#################### splash screen mode ####################

from tkinter import filedialog


def splashScreenMousePressed(event,data):
    if 260<=event.y<=500:
        if 440<=event.x<=710:
            data.mode="chooseImage"
        elif 790<=event.x<=1060:
            data.mode="draw"
        elif 90<=event.x<=360:
            data.fileName = filedialog.askopenfilename(initialdir="/",\
            title="Choose an image",filetypes=(("GIF", ".gif"),("all files","*.*")))
            index = -data.fileName[::-1].find("/")
            name = data.fileName[index:]
            data.imageFile = PhotoImage(file=name)
            data.Character.image = data.imageFile.subsample(3,3)

    if 1090<=event.x<=1180 and 590<=event.y<=670:
        data.mode="play"

    if 30<=event.x<=160 and 550<=event.y<=670:
        data.mode="help"

def splashScreenKeyPressed(event,data):
    pass

def splashScreenTimerFired(data):
    pass

def splashScreenRedrawAll(canvas,data):
    canvas.create_image(data.width/2,data.height/2,image=data.splashBackground)
    canvas.create_text(data.width/2,150,text="Welcome to Avocado!",font="Chalkduster 80",fill="white")

    a = 370
    canvas.create_image(300,a,image=data.cloud)

    canvas.create_text(228,a,text="Upload a picture",font="Chalkduster 23")

    canvas.create_image(650,a,image=data.cloud)

    canvas.create_text(580,a,text="Choose from \n    gallery",font="Chalkduster 23")

    canvas.create_image(1000,a,image=data.cloud)
    canvas.create_text(930,a,text="Draw a picture",font="Chalkduster 23")

    canvas.create_image(data.width-40,data.height-70,image=data.cloud1)
    canvas.create_text(data.width-65,data.height-70,text="OK",font="Chalkduster 23")

    canvas.create_image(130,data.height-90,image=data.imageCloud)
    canvas.create_text(100,data.height-90,text="Need \nhelp?",font="Chalkduster 20")


#################### draw mode ####################

def drawMousePressed(event,data):

    if data.BackButton.clickWithin(event):
        data.mode = "splashScreen"

    elif data.Red1.clickWithin(event):
        data.drawColor = "red"

    elif data.Blue1.clickWithin(event):
        data.drawColor = "blue"

    elif data.Green1.clickWithin(event):
        data.drawColor = "green"

    elif data.Yellow1.clickWithin(event):
        data.drawColor = "yellow"

    elif data.Black1.clickWithin(event):
        data.drawColor = "black"

    elif data.White1.clickWithin(event):
        data.drawColor = "white"

    elif data.ClearButtonDraw.clickWithin(event):
        data.drawShape = []
        data.penPos = []
        data.penDraw = []

    for shape in data.drawShape:
        if shape.clickWithin(event):
            shape.cx,shape.cy = event.x,event.y
            data.onShape[shape] = True

    if data.Circle.clickWithin(event):
        data.newCircle = Circle(data.Circle.cx,data.Circle.cy,data.Circle.r,data.drawColor)
        data.newCircle.cx,data.newCircle.cy = event.x,event.y
        data.drawShape.append(data.newCircle)

    elif data.Square.clickWithin(event):
        data.newSquare = Square(data.Square.cx,data.Square.cy,data.Square.r,data.drawColor)
        data.newSquare.cx,data.newSquare.cy = event.x,event.y
        data.drawShape.append(data.newSquare)

    elif data.Triangle.clickWithin(event):
        data.newTriangle = Triangle(data.Triangle.cx,data.Triangle.cy,data.Triangle.r,data.drawColor)
        data.newTriangle.cx,data.newTriangle.cy = event.x,event.y
        data.drawShape.append(data.newTriangle)

    if 810<=event.x<=890 and 590<=event.y<=630:
        data.isPen = True

    elif not data.picBoard.clickWithin(event):
        data.isPen = False


    if data.isPen and data.picBoard.clickWithin(event):
        data.drawPen = Pen(event.x,event.y,2,data.drawColor)
        data.drawShape.append(data.drawPen)
        data.penPos.append((event.x,event.y,data.drawColor))



def drawMouseMoved(event,data):
    canvas = event.widget.canvas

    if not data.isPen:
        for shape in data.onShape:
            if data.onShape[shape]:
                shape.cx,shape.cy = event.x,event.y

    if data.isPen:
        data.penPos.append((event.x,event.y,data.drawColor))

def drawMouseReleased(event,data):
    canvas = event.widget.canvas
    for key in data.onShape:
        data.onShape[key] = False


def drawKeyPressed(event,data):

    for stuff in data.onShape:
        if data.onShape[stuff]:
            if event.keysym == "Up":
                stuff.r += 5
            elif event.keysym == "Down":
                stuff.r -= 5

def drawTimerFired(data):
    pass

def drawRedrawAll(canvas,data):

    canvas.create_image(data.width/2,data.height/2,image=data.drawBackground)

    canvas.create_text(data.width/2,100,text="Have fun drawing!",font="Phosphate 60")
    data.BackButton.draw(canvas)
    data.picBoard.draw(canvas)
    data.ToolBoard.draw(canvas)
    data.Red1.draw(canvas)
    data.Blue1.draw(canvas)
    data.Green1.draw(canvas)
    data.Yellow1.draw(canvas)
    data.Black1.draw(canvas)
    data.White1.draw(canvas)
    data.Circle.draw(canvas)
    data.Square.draw(canvas)
    data.Triangle.draw(canvas)
    canvas.create_image(850,610,image=data.pen)

    data.ClearButtonDraw.draw(canvas)

    instruction = '''(How to change the size of the shape: click on the shape, hold the mouse,\n and hit "up" key to make it bigger, or hit "down" key to make it smaller)'''
    canvas.create_text(290,620,text=instruction,font="Klee 12")
    canvas.create_text(320,190,text="Drag the shapes here!",font="Klee 12")

    for shape in data.drawShape:
        if data.picBoard.dropIn(shape):
            shape.draw(canvas)

    if data.isPen:

        for i in range(len(data.penPos)-1):
            x0,y0,color0 = data.penPos[i]
            x1,y1,color1 = data.penPos[i+1]
            data.penDraw.append([(x0,y0),(x1,y1),color0])


    for point in data.penDraw:
        canvas.create_line(point[0],point[1],width=5,fill=point[2])


#################### help mode ####################

def helpMousePressed(event,data):
    if data.BackButton.clickWithin(event):
        data.mode="splashScreen"

def helpKeyPressed(event,data):
    pass

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas,data):

    canvas.create_image(data.width/2,data.height/2,image=data.helpBackground)
    data.BackButton.draw(canvas)
    canvas.create_text(data.width/2,80,text="What is Avocado?",font="Phosphate 60")
    general = "Avocado is a simple programming language for kids or new programmers.\nIt is inspired by Scratch. By using Avocado, users can get a general idea\nof how coding looks like. Instructions are shown to guide users."
    canvas.create_text(data.width/2,180,text=general,font="Klee 28 bold")

    canvas.create_text(270,290,text="Upload a picture:",font="Chalkduster 30")
    upload = "You could upload your favorite picture here and\nwatch it moving!"
    canvas.create_text(760,305,text=upload,font="Klee 28 bold")

    canvas.create_text(305,390,text="Choose from gallery:",font="Chalkduster 30")
    choose = "Or just simply choose from our favorite\ncharacters in the gallery and get started!"
    canvas.create_text(780,405,text=choose,font="Klee 28 bold")
    
    canvas.create_text(255,490,text="Draw a picture:",font="Chalkduster 30")
    draw = "In this simple drawing tool, you get to play around\n with shapes and colors!"
    canvas.create_text(740,505,text=draw,font="Klee 28 bold")
    canvas.create_text(data.width/2,data.height-90,text="Everyone can code!",font="Chalkduster 40")



# adapted from http://www.cs.cmu.edu/~112/notes/events-example0.py

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)

        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    root = Tk()

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 
    init(data)

    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    root.canvas = canvas.canvas = canvas    

    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<B1-Motion>", lambda event: drawMouseMoved(event,data))
    root.bind("<B1-ButtonRelease>", lambda event: drawMouseReleased(event,data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))

    timerFiredWrapper(canvas, data)

    root.mainloop()  
    print("bye!")

run(1200, 700)

from pyautogui import *
import random
from time import sleep
random.seed()
GoList=[]
class Place():
    def __init__(self,name):
        self.cango=[]
        self.name=name
    def ap(self,a):
        self.cango.append(a)
    def search(self,goPlace):
        for i in self.cango:
            if i==goPlace.name:
                GoList.append(goPlace.name)
                return True
            else:
                if(i.search(goPlace)):
                    GoList.append(i)
                    return True
        return False
def globalClean():
    GoList.clear()
def cokey(a,b):
    keyDown(a)
    press(b)
    keyUp(a)
def mouse2(a,b):
    c, d = position()
    time=1
    while(c!=a or d!=b):
        time+=1
        print(time)
        c, d = position()
        if(abs(c-a)<10 and abs(d-b)<10):
            moveTo(a,b)
            break
        tempX,tempY=a-c,b-d
        p=random.random()*5
        dir1=random.random()
        dir2=random.random()
        print(dir1,dir2)
        if(dir1>0.5):
            dir1=1
        else:
            dir1=-1
        if(dir2>0.5):
            dir2=1
        else:
            dir2=-1
        moveTo(c+tempX/15+p*dir1,d+tempY/15+p*dir2)
        # sleep(1.0/100.0)
def IsThere(str):
    if (str=='123'):
        pass
def GetRandomPoint(x1,y1,x2,y2):
    pass
from pyautogui import *
import random
from time import sleep
random.seed()
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
        moveTo(c+tempX/3+p,d+tempY/3+p)
        sleep(0.001)


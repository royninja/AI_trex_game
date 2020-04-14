# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:05:07 2020

@author: Sayan Roy
"""

from PIL import ImageGrab
from PIL import ImageOps
from numpy import *
import pyautogui
import time
class Cordinates:
    # restart button for fullscreen 681 and for half screen 340
    restart=(340,390)
    #diano pos 
    diano=(172,440) #395
      
def restartGame():
    pyautogui.click(Cordinates.restart)
    pyautogui.keyDown('down')

def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    time.sleep(0.18)
    pyautogui.keyUp('sapce')
    pyautogui.keyDown('down')
    
def imageGrab():
    box=(Cordinates.diano[0]+60,Cordinates.diano[1],Cordinates.diano[0]+100,Cordinates.diano[1]+5)
    image=ImageGrab.grab(box)
    grayImg=ImageOps.grayscale(image)
    a=array(grayImg.getcolors())
    print(a.sum())
    return a.sum()  
    
    
def main():
    restartGame()
    while True:
        if(imageGrab()!=447):
            pressSpace()
            time.sleep(0.1)


main()
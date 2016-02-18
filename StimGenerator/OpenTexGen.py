'''
Created on 2016-02-17

@author: Tomy
'''
import os
import time
from shutil import copyfile
emplacement = "C:\Exp"
files_names = os.listdir(emplacement)

nombre_de_stimuli = 0

os.startfile("C:\Exp\Texture 2.trd")
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
time.sleep(5)


while nombre_de_stimuli < 10 :
    click(170,40)
    click(170,48)
    time.sleep(12)
    click(688,430)
    for x in files_names:
        if x.startswith("Texture 2_A000500"):
            number = 1
            file_name = x
            for y in os.listdir("C:\Exp\TextureTest") :
                if y[0 : len(y)-4] == "TextureA" :
                    number += 1
                elif y[0 : len(y)-5] == "TextureA" :
                    number += 1
                elif y[0 : len(y)-6] == "TextureA" :
                    number += 1
                elif y[0 : len(y)-7] == "TextureA" :
                    number += 1
            copyfile("C:\Exp\%s" % file_name, "C:\Exp\TextureTest\TextureA%s.bmp" % number)
        elif x.startswith("Texture 2_A000900"):
            number = 1
            file_name = x
            for y in os.listdir("C:\Exp\TextureTest") :
                if y[0 : len(y)-4] == "TextureB" :
                    number += 1
                elif y[0 : len(y)-5] == "TextureB" :
                    number += 1
                elif y[0 : len(y)-6] == "TextureB" :
                    number += 1
                elif y[0 : len(y)-7] == "TextureB" :
                    number += 1
            copyfile("C:\Exp\%s" % file_name, "C:\Exp\TextureTest\TextureB%s.bmp" % number)
        elif x.startswith("Texture 2_A000700"):
            number = 1
            file_name = x
            for y in os.listdir("C:\Exp\TextureTest") :
                if y[0 : len(y)-4] == "TextureC" :
                    number += 1
                elif y[0 : len(y)-5] == "TextureC" :
                    number += 1
                elif y[0 : len(y)-6] == "TextureC" :
                    number += 1
                elif y[0 : len(y)-7] == "TextureC" :
                    number += 1
            copyfile("C:\Exp\%s" % file_name, "C:\Exp\TextureTest\TextureC%s.bmp" % number)
    
    nombre_de_stimuli += 1
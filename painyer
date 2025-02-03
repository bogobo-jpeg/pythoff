import turtle
import pyautogui
import keyboard
from PIL import Image
import os
import sys
t = turtle
t.speed(99999999999999)
t.penup()
t.bk(700)
size = 1
pen = 0
while True:
    if keyboard.is_pressed('e'):
        pen = 1
    if keyboard.is_pressed('+'):
        size += 1
    if keyboard.is_pressed('-'):
        size -= 1
    if keyboard.is_pressed('c'):
        color = input("color? ")
        t.color(color)
    if keyboard.is_pressed('p'):
        art = pyautogui.screenshot("art.png")
        script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 
        art3 = ("\\art.png")
        save = ("saved in ")
        print(save + script_directory + art3)
        t.done()
    x, y = pyautogui.position()
    pos = (x - 670,y - y * 2 + 360)
    print(pos)
    t.goto(pos)
    if pen == 0:
        t.penup()
    if pen == 1:
        t.pendown()
    t.pensize(size)
    pen = 0
    print(pen)




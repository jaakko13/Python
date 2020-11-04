from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

# black color is (17, 17, 17)
# Position of tile rows = 
# 1. (794, 650)
# 2. (903, 650)
# 3. (1002, 650)
# 4. (1092, 650)

# Used to display location and rgb color of tiles
pyautogui.displayMousePosition()


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(794, 650) [0] == 30:
        click(794, 650)

    if pyautogui.pixel(903, 650) [0] == 30:
        click(903, 650)

    if pyautogui.pixel(1002, 650) [0] == 30:
        click(1002, 650)

    if pyautogui.pixel(1092, 650) [0] == 30:
        click(1092, 650)
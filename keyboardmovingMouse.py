from pyautogui import *
import keyboard
import pyautogui
import win32api
import win32con



def moveLeft():
    if keyboard.is_pressed('a'):
        pyautogui.move(-10,0)

def moveRight():
    if keyboard.is_pressed('d'):
        pyautogui.move(10,0)

def moveUp():
    if keyboard.is_pressed('w'):
        pyautogui.move(0,-10)

def moveDown():
    if keyboard.is_pressed('s'):
        pyautogui.move(0,10)


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def RightClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)



while keyboard.is_pressed('q') == False: # Press q to close script

    while keyboard.is_pressed('a'):
        moveLeft()

    while keyboard.is_pressed('d'):
        moveRight()

    while keyboard.is_pressed('w'):
        moveUp()

    while keyboard.is_pressed('s'):
        moveDown()

    if keyboard.is_pressed('e'):
        click()

    if keyboard.is_pressed('r'):
        RightClick()

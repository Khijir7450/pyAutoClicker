import pyautogui as pag
import time
import keyboard


time.sleep(3)

def getInputPosition():
    positions = []
    
    print('press "x" key to lock position...')
    while True:
        # Check if x key is pressed
        time.sleep(0.1)

        if keyboard.is_pressed('x'):
            print('x key pressed...')
            break
    
     # Get the current mouse position
    x, y = pag.position()
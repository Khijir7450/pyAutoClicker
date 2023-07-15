import pyautogui as pag
import time
import keyboard


# print("Enter how many position you want to click: ")
# noOfPosition = input()

# print("Enter time difference between two click(sec): ")
# sleepTime =input()


def getInputPosition(noOfPosition):
    INPUT_COUNT =noOfPosition
    positions = []
    
    print('Fix mouse position and press "space bar" key to lock  position...')
    while (INPUT_COUNT > 0):
        # Check if x key is pressed
        time.sleep(0.1)

        if keyboard.is_pressed('space'):
            
            t_pos = pag.position()
            positions.append(t_pos)
            INPUT_COUNT -= 1
            time.sleep(0.1)
            print("Position selected: ", t_pos)
            
            print('Fix mouse position and press "space bar" key to lock position...')
            
            
            
            
    return positions


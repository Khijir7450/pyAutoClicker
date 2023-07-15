import pyautogui as pag
import time
import keyboard

def getInputPosition():
    INPUT_COUNT = 2
    positions = []
    
    print('press "space bar" key to lock position...')
    while (INPUT_COUNT > 0):
        # Check if x key is pressed
        time.sleep(0.1)

        if keyboard.is_pressed('space  '):
            print('x key pressed...')
            t_pos = pag.position()
            positions.append(t_pos)
            INPUT_COUNT -= 1
            print("Change mouse position to choose another position")
            time.sleep(0.7)
            
            
    return positions


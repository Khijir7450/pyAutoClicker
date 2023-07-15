import pyautogui as pag  

import time
import keyboard
from userInput import getInputPosition



def clicky(sleepTime, noOfPosition):
    positionToClick = getInputPosition(noOfPosition)



    print("For start press 'Enter' :")
    isRunning  = True
    while isRunning:
        if keyboard.is_pressed('Enter'):
            for i in positionToClick:
                pag.click(i)
                time.sleep(sleepTime)
                
            
            isRunning = False  
        
        
    
     

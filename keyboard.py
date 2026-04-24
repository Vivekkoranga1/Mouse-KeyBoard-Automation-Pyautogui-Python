##In mouse.py we have learn how to control mouse with python 
##In this we weill learn how to control keyboard with python and we will write inside main.txt 

## i have created keyboard.py so location of main.txt is changed 
##so i will write code to move mouse to main.txt and open main.txt

import pyautogui


##opening main.txt mouse automation part
x,y = 127,159    
pyautogui.doubleClick(x,y)




##keyboard part writing Hey i am vivek to new file main.txt
pyautogui.write("Hey i am vivek")

##keyboard part writing at end of text if text already exist in the file 
pyautogui.press("down")
pyautogui.press("enter") #for new line 
pyautogui.write("I know you are vivek")
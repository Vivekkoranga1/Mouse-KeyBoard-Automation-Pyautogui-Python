##mouse automation using pyautogui for windows for mac code can be slightly change or you will have to give permission

import pyautogui

##print current mouse position 
mouse_position = pyautogui.position()
#print(mouse_position)

##find position of main.txt to perform mouse_automation
##first keep your cursor on main.txt
##then run script via short cut key or like me open terminal and place cursor on main.txt and type python mouse.py (windows)
##i am  getting this Point(x=136, y=159) where my main.txt

##move cursor from anywhere to main.txt 
##pyautogui.moveTo(136,159) ##this is quite fast

pyautogui.moveTo(136,159,duration=5) ##now it will go slowly there in 5 seconds

#opening file (main.txt)
pyautogui.click() ##single click for double click pyautogui.click(clicks=2) or pyautogui.doubleClick()
##Here in pyautogui.click() we are clicking at current position 
##current posiiton is  (136,159) because we are moving to that postion using line no 15 pyautogui.moveTo(136,159,duration=5)
## instead we can do #pyautogui.click(136,159) providing cordinates to click directly ortherwise it will click at current postiion

##by defauult click uses left click
##left_click using click function
# pyautogui.click(button="right")

#don't be get cnfused between move and moveTo
#pyautogui.move(100,0) it will take cursor 100 pixel right from current postion becuase x = 100 and y = 0


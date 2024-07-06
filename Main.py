import pyautogui as pg
import time

codebox = (415,870)

"Check for sections with different title names. The size difference may cause it to bug out. Set for warmup-1 now. Screen zoom:100%"
title = (245,336)

next = (136,369)

"Change this number as required"
n=8

time.sleep(7)

for i in range(n):
    #Copy the code and paste it in notepad
    pg.moveTo(codebox, duration=0.2)
    pg.click()
    pg.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pg.hotkey('ctrl', 'c')
    pg.hotkey('alt', 'tab')
    time.sleep(0.7)
    pg.hotkey('ctrl', 'v')
    time.sleep(0.7)

    #save menu
    pg.hotkey('ctrl', 'shift', 's')
    time.sleep(1)

    #get the name of the program
    pg.hotkey('alt', 'tab')
    pg.moveTo(title, duration=0.2)
    pg.doubleClick()
    pg.hotkey('ctrl', 'c')

    #paste the title as the file's name
    pg.hotkey('alt', 'tab')
    time.sleep(1)
    pg.hotkey('ctrl', 'v')
    time.sleep(0.5)
    #pg.hotkey('left')
    pg.typewrite('.py',0.15)

    #save it, close this window, open a new one
    pg.hotkey('alt', 's')
    time.sleep(1)
    "I keep a tab open and close the new one. Otherwise it'll just be a clutter of tabs. If youre gonna close the tab using the next line keep an additional tab open !!"
    #pg.hotkey('ctrl', 'w')
    time.sleep(0.5)
    pg.hotkey('ctrl', 'n')

    #back to codingbat and allover again
    pg.hotkey('alt', 'tab')
    pg.moveTo(next, duration=0.2)
    pg.click()
    time.sleep(3)


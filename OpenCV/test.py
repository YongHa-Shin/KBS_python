from turtle import position
import pyautogui as pag
import time

while True:

    pag.moveTo(2700, 520)
    pag.click()
    time.sleep(0.5)
    pag.press('left')
    time.sleep(5)
    # pag.keyDown('left')
    # pag.keyUp('left')
    # pag.press('left')
    # pag.typewrite(['left'])

    
    # x, y = pag.position()
    # position_str = 'X: ' + str(x) + ' Y: ' + str(y)
    # print(position_str)


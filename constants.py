API_KEY='5581771112:AAGxKriRBk_3Ak67lBCaeNA4vbgeH-tDwkU'


import pyautogui as pg
import time
count=1
while count<=100:
    pg.click(581,983)
    time.sleep(0.1)
    pg.write('Testing')
    pg.press('enter')
    count+=1




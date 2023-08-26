# Script that perform normal updating of a repo

import os
import pyautogui

username = 'AhmedH1st'
password = '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'

os.system("git add .")
os.system('git commit -m "updating repo"')
os.system('git push')

pyautogui.sleep(5)

pyautogui.typewrite(username)
pyautogui.press('enter')
pyautogui.typewrite(password)
pyautogui.press('enter')


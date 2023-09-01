# Script to open Gmail and convert all emails from unread status to read
import webbrowser
import pyautogui
import time

349, 199
webbrowser.open("www.gmail.com")
time.sleep(10)
pyautogui.click(349, 199)
time.sleep(1)
pyautogui.click('mail.png')
time.sleep(1)
pyautogui.click(349, 199)

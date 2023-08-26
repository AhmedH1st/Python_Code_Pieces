import pyautogui
import os.path


# this line saves the path of the image called 'term' in a "imgPath" string
imgPath = os.path.dirname(__file__)+"/term"

imgFound = None


while imgFound is None:
    imgFound = pyautogui.locateOnScreen(imgPath)

print('FOUND') 

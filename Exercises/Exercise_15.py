# Script to setup extensions in VS code
import pyautogui
import json


def reset_search_bar():
    pyautogui.click(locations_dic['search_bar_loc']
                    [0], locations_dic['search_bar_loc'][1])
    pyautogui.sleep(1)
    for i in range(15):
        pyautogui.press('backspace')


def install():
    pyautogui.click(locations_dic['first_extension_installButton_loc']
                    [0], locations_dic['first_extension_installButton_loc'][1])
    pyautogui.sleep(4)


Locations_file_path = "/home/ahmedh/Desktop/Trials/Python_Exercises/locations_on_screen.txt"

# open the file which contains the location of each button on screen
f = open(Locations_file_path, 'r')

# read the file and parse its data to a dictionary
lines_str = ''
lines_str = lines_str.join(f.readlines())
lines_str = lines_str.strip().replace('\n', '').replace(' ', '')
locations_dic = json.loads(lines_str)

pyautogui.click(locations_dic['vs_code_loc'][0],
                locations_dic['vs_code_loc'][1])
pyautogui.sleep(10)

pyautogui.click(locations_dic['extensions_button_loc'][0],
                locations_dic['extensions_button_loc'][1])
pyautogui.sleep(2)

pyautogui.click(locations_dic['search_bar_loc'][0],
                locations_dic['search_bar_loc'][1])
pyautogui.sleep(2)

pyautogui.typewrite("clangd")
pyautogui.sleep(7)

install()
reset_search_bar()

pyautogui.typewrite("c++ test")
pyautogui.sleep(5)

install()
reset_search_bar()

pyautogui.typewrite("c++ helper")
pyautogui.sleep(5)

install()
reset_search_bar()

pyautogui.typewrite("cmake")
pyautogui.sleep(5)

install()
reset_search_bar()

pyautogui.typewrite("cmake tools")
pyautogui.sleep(5)

install()
reset_search_bar()

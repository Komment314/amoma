import keyboard
import pyautogui
import os

screenshot_num = 0

PICS_DIR = os.path.join(os.getcwd(), "pics")
os.makedirs(PICS_DIR, exist_ok=True)


def make_screenshot():
    global screenshot_num
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(os.path.join(PICS_DIR, str(screenshot_num) + '.png'))
    screenshot_num += 1


keyboard.add_hotkey('Ctrl + 1', make_screenshot)


keyboard.wait('Alt + q')

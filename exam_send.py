import pyautogui
import time
import os

from sqlalchemy import true


PICS_DIR = os.path.join(os.getcwd(), "pics")
SEND_TO_GIT_SCRIPT = os.path.join(os.getcwd(), "send.sh")

DELAY = 0  # Задержка перед тем, как программа начёнет делать скриншоты
SLEEP_TIME = 30  # Промежуток в секундах между коммитами

time.sleep(DELAY)

while true:
    os.system(SEND_TO_GIT_SCRIPT)
    time.sleep(SLEEP_TIME)



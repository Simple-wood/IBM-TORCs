import subprocess
import pyautogui
import time
import experimental
from logger import LogData

TORCS_PATH = r"ADD path to wtorcs"
WORKING_DIRECTORY_PATH = r"ADD working directory path for TORCs"
CLICK_X = 399 # Based on 640x480 resolution
CLICK_Y = 144 # Based on 640x480 resolution
STEPS = 10

# Opens torcs and runs the drive script
#
def start_lap():
    logger  = LogData()
    subprocess.Popen(TORCS_PATH,
                    cwd=WORKING_DIRECTORY_PATH)

    time.sleep(10)
    pyautogui.moveTo(CLICK_X, CLICK_Y)
    pyautogui.doubleClick()
    pyautogui.click()

    with pyautogui.hold('shift'):
        pyautogui.press('+', presses=7)
    
    experimental.run_lap(logger)

for x in range(STEPS):
    start_lap()


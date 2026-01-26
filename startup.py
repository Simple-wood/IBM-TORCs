import subprocess
import pyautogui
import time
import experimental
from logger import LogData

TORCS_PATH = r"c:\Users\joesa\Downloads\torcs (1)\torcs\wtorcs.exe"
WORKING_DIRECTORY_PATH = r"c:\Users\joesa\Downloads\torcs (1)\torcs"
CLICK_X = 399
CLICK_Y = 144
STEPS = 15

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
    
    experimental.run_lap(logger)

for x in range(STEPS):
    start_lap()

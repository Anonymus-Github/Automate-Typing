import pyautogui
import time

code_to_type = """
Remove this line and paste your code here
"""

# Time in seconds before auto typing starts (make sure that your text cursor is placed in the text box where you want to auto type the code)
wait_time = 2
time.sleep(wait_time)

# Time interval between entering characters
time_interval = 0.00001


def avoid_auto_complete():
    '''Hotkey to avoid auto completion and indentation'''
    pyautogui.hotkey('space', 'backspace', 'enter', 'space', 'ctrl', 'left')


lines = list(code_to_type.split("\n"))
for line in lines:
    if line != "":
        pyautogui.typewrite(line, interval = time_interval)
        avoid_auto_complete()
    else:
      pyautogui.press('enter')

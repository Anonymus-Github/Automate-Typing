import pyautogui
import time

code_to_type = """
# Educational Codeforces Round 130 (Rated for Div. 2) C
def check_a(i, s, t):
    n = len(s)
    sc = {'a':0, 'b':0, 'c':0}
    tc = {'a':0, 'b':0, 'c':0}
    while i<n:
        if sc['a'] < tc['a'] or sc['c'] >= 1 or tc['c'] >= 1:
            return (False, i)
        sc[s[i]] += 1
        tc[t[i]] += 1
        i += 1
        if sc == tc:
            return (True, i)
    if sc != tc or sc['c'] >= 1 or tc['c'] >= 1:
        return (False, i)
    return (True, i)
def check_c(i, s, t):
    n = len(s)
    sc = {'a':0, 'b':0, 'c':0}
    tc = {'a':0, 'b':0, 'c':0}
    while i<n:
        if sc['b'] < tc['b'] or sc['a'] >= 1 or tc['a'] >= 1:
            return (False, i)
        sc[s[i]] += 1
        tc[t[i]] += 1
        i += 1
        if sc == tc:
            return (True, i)
    if sc != tc or sc['a'] >= 1 or tc['a'] >= 1:
        return (False, i)
    return (True, i)
def solve():
    n = int(input())
    s = input()
    t = input()
    i = 0
    while i<n:
        if s[i] == t[i]:
            i += 1
        else:
            if s[i] == 'a' or t[i] == 'a':
                temp = check_a(i, s, t)
            else:
                temp = check_c(i, s, t)
            if temp[0] == False:
                print("NO")
                return
            i = temp[1]
    print("YES")
for _ in range(int(input())):
    solve()
"""

# Time in seconds before auto typing starts (make sure that your text cursor is placed in the text box where you want to auto type the code)
wait_time = 2
time.sleep(wait_time)

# Time interval between entering characters
time_interval = 0.00001


def avoid_auto_complete():
    '''Hotkey to avoid auto completion and indentation'''
    pyautogui.hotkey('esc', 'space', 'backspace', 'enter', 'space', 'ctrl', 'left')


lines = list(code_to_type.split("\n"))
for line in lines:
    if line != "":
        pyautogui.typewrite(line, interval=time_interval)
        avoid_auto_complete()
    else:
        pyautogui.press('enter')

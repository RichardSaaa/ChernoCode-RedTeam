import pyautogui
import time

#Primeira Fase > Abrir o Chrome
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

time.sleep(3)
test = pyautogui.hotkey("ctrl", "t")

for test in range(1000):
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write("https://www.xxx.com")
    pyautogui.press("enter")

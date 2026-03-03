import pyautogui
import time
import webbrowser


pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("bloco de notas")
pyautogui.press("enter")

frase = "Eu sei o que voce fez no verao passado"

pyautogui.write(frase, interval=0.2)

time.sleep(2)

pyautogui.hotkey("alt", "f4")
pyautogui.press("tab")
pyautogui.press("enter")

url = "http://127.0.0.1:5500/index.html"
webbrowser.open(url)
time.sleep(0.1)
pyautogui.press("f11")








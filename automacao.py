import webbrowser
import pyautogui
from time import sleep
import json

with open("telefones.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    telefones = data["telefones"]

for telefone in telefones:
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(f"https://api.whatsapp.com/send?phone={telefone}")
    sleep(10)
    pyautogui.click(1077,305, duration=1)
    sleep(10)
    pyautogui.typewrite('Mensagem que voce deseja enviar')
    sleep(5)
    pyautogui.press('Enter')
    sleep(300)

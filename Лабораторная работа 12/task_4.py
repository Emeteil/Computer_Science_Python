import PySimpleGUI as sg
import threading
import random

from requests.exceptions import *
import requests

def random_org(a: int, b: int) -> int:
    try:
        response = requests.get(
            "https://www.random.org/integers",
            params = {
                "num": 1,
                "min": a,
                "max": b,
                "col": 1,
                "base": 10,
                "format": "plain",
            }
        )

        response.raise_for_status()

        return int(response.text)
    except (ConnectionError, HTTPError):
        return 0

def generate_http(window, values) -> None:
    window["OUTPUT"].update(f"Считаем...")
    window["MAIN_BUTTON"].update(disabled = True)
    min = int(values["MIN_GENERATE"])
    max = int(values["MAX_GENERATE"])
    
    def random_org_thread():
        global result
        result = random_org(min, max)
        window["OUTPUT"].update(f"{result}")
        window["MAIN_BUTTON"].update(disabled = False)
    
    thread = threading.Thread(target = random_org_thread)
    thread.start()

def generate_lib(window, values) -> None:
    min = int(values["MIN_GENERATE"])
    max = int(values["MAX_GENERATE"])
    
    result = random.randint(min, max)
    window["OUTPUT"].update(f"{result}")

def main():
    sg.theme("Dark Grey 15")
    layout = [[
        sg.Column(
            [
                [sg.Image(source = "task_4.jpg", size = (275, 275))],
                [
                    sg.Text("Границы рандома"),
                    sg.InputText(default_text = "0", size = (5, 1), key = "MIN_GENERATE"),
                    sg.InputText(default_text = "100", size = (5, 1), key = "MAX_GENERATE")
                ],
                [
                    sg.Radio("Псевдорандом", "RADIO1", default = True, key = "RANDOM_LIB"),
                    sg.Radio("random.org", "RADIO1", key="RANDOM_ORG")
                ],
                [sg.Button("Сгенерировать", size = (15, 2), key = "MAIN_BUTTON")],
                [sg.Text("Нажми на кнопку", key = "OUTPUT", justification = 'center')]
            ],
            element_justification = 'center',
            justification = 'center',
        )
    ]]
    
    window = sg.Window("Рандомайзер", layout, size = (300, 430), icon = "task_4.ico")
    
    while True:
        event, values = window.read()
        try:
            match event:
                case "MAIN_BUTTON":                    
                    if values["RANDOM_LIB"]:
                        generate_lib(window, values)
                        continue
                    
                    generate_http(window, values)
                case sg.WIN_CLOSED: break
                case _: pass
        except ValueError:
            window["OUTPUT"].update("Некоректные данные!")
        except Exception as e:
            window["OUTPUT"].update(str(e))

if __name__ == "__main__":
    main()
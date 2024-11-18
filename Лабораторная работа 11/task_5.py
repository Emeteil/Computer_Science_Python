import PySimpleGUI as sg
import threading
import time

letters = {
    1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

score_dir = {}
for k, v in letters.items():
    for c in v:
        score_dir[c.lower()] = k

def calculate(window, values) -> None:
    word_origin: str = values["WORD"]
    word: str = word_origin.lower()
    
    window["MAIN_BUTTON"].update(disabled = True)
    
    if not word:
        window["OUTPUT"].update("Поле не должно быть пустым!")
        window["MAIN_BUTTON"].update(disabled = False)
        return
    
    def random_org_thread():
        window["OUTPUT"].update(word_origin)
        time.sleep(0.4)
        window["OUTPUT"].update(" ".join(word_origin))
        time.sleep(0.4)
        window["OUTPUT"].update(" + ".join(word_origin))
        time.sleep(0.4)
        
        score = sum(score_dir.get(c, 0) for c in word)
        numbes: list[str] = [str(score_dir.get(c, 0)) for c in word]
        for i in range(len(word)):
            for _ in range(2): 
                for j in range(1, 3 + 1):
                    window["OUTPUT"].update(
                        (' + '.join(numbes[:i])) +
                        (' + ' if i != 0 else '') +
                        ('.' * j) +
                        (' + ' if i != len(word) - 1 else '') +
                        (' + '.join(word_origin[i + 1:]))
                    )
                    time.sleep(0.2)
        
        
        window["OUTPUT"].update(' + '.join(numbes))
        time.sleep(0.7)
        string = f"Слово стоит {score} очков"
        for i in range(len(string)):
            window["OUTPUT"].update(string[0:i + 1])
            time.sleep(0.07)
                
        window["MAIN_BUTTON"].update(disabled = False)
    
    thread = threading.Thread(target = random_org_thread)
    thread.start()

def main():    
    sg.theme("Dark Grey 15")
    layout = [[
        sg.Column(
            [
                [sg.Image(source = "task_5.png", size = (275, 275))],
                [
                    sg.Text("Слово"),
                    sg.InputText(default_text = "Hello", size = (15, 1), key = "WORD"),
                ],
                [sg.Button("Посчитать", size = (15, 2), key = "MAIN_BUTTON")],
                [sg.Text("Нажми на кнопку", key = "OUTPUT", justification = 'center')]
            ],
            element_justification = 'center',
            justification = 'center',
        )
    ]]
    
    window = sg.Window("Эрудит", layout, size = (300, 400), icon = "task_5.ico")
    
    while True:
        event, values = window.read()
        try:
            match event:
                case "MAIN_BUTTON":
                    calculate(window, values)
                case sg.WIN_CLOSED: break
                case _: pass
        except ValueError:
            window["OUTPUT"].update("Некоректные данные!")
        except Exception as e:
            window["OUTPUT"].update(str(e))

if __name__ == "__main__":
    main()
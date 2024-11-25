import PySimpleGUI as sg

def number_to_direct(num: int) -> str:
    if not (-128 <= num <= 127):
        raise ValueError("number not in (-128, 127)")
    
    return bin(num & 255)[2:].zfill(8)

def number_to_return(num: int) -> str:
    if not (-128 <= num <= 127):
        raise ValueError("number not in (-128, 127)")
    
    return bin(~num & 255)[2:].zfill(8)

def number_to_additional(num: int) -> str:
    if not (-128 <= num <= 127):
        raise ValueError("number not in (-128, 127)")
    
    return bin((~num + 1) & 255)[2:].zfill(8)

def binary_to_int(num: str) -> int:
    if any(i not in "01" for i in num):
        raise ValueError("number non-binary")
    
    if num[0] == '0': return int(num, 2)
    return -((~int(num, 2) & 255) + 1)
    
def convert_numbers(window, values) -> None:
    number = int(values["NUMBER"])
    
    direct_code: str = number_to_direct(number)
    return_code: str = number_to_return(number)
    additional_code: str = number_to_additional(number)
    
    window["DIRECT_CODE"].update(direct_code)
    window["DIRECT_CODE_INT"].update(binary_to_int(direct_code))
    
    window["RETURN_CODE"].update(return_code)
    window["RETURN_CODE_INT"].update(binary_to_int(return_code))
    
    window["ADDITIONAL_CODE"].update(additional_code)
    window["ADDITIONAL_CODE_INT"].update(binary_to_int(additional_code))
    window["OUTPUT"].update("")

def main():
    sg.theme("Dark Grey 15")
    layout = [[
        sg.Column(
            [
                [sg.Image(source = "task_4.jpg", size = (275, 275))],
                [sg.Text("Число")],
                [
                    sg.InputText(default_text = "", size = (15, 1), key = "NUMBER")
                ],
                [sg.Text("Прямой код")],
                [
                    sg.InputText(default_text = "", readonly = True, size = (10, 1), key = "DIRECT_CODE"),
                    sg.InputText(default_text = "", readonly = True, size = (4, 1), key = "DIRECT_CODE_INT")
                ],
                [sg.Text("Обратный код")],
                [
                    sg.InputText(default_text = "", readonly = True, size = (10, 1), key = "RETURN_CODE"),
                    sg.InputText(default_text = "", readonly = True, size = (4, 1), key = "RETURN_CODE_INT")
                ],
                [sg.Text("Дополнительный код")],
                [
                    sg.InputText(default_text = "", readonly = True, size = (10, 1), key = "ADDITIONAL_CODE"),
                    sg.InputText(default_text = "", readonly = True, size = (4, 1), key = "ADDITIONAL_CODE_INT")
                ],
                [sg.Button("Перевести", size = (15, 2), key = "MAIN_BUTTON")],
                [sg.Text("", key = "OUTPUT", justification = 'center')]
            ],
            element_justification = 'center',
            justification = 'center',
        )
    ]]
    
    window = sg.Window("Байт", layout, size = (300, 430), icon = "task_4.ico")
    
    while True:
        event, values = window.read()
        try:
            match event:
                case "MAIN_BUTTON":                    
                    convert_numbers(window, values)
                case sg.WIN_CLOSED: break
                case _: pass
        except ValueError as e:
            window["OUTPUT"].update("Некоректные данные!")
        except Exception as e:
            window["OUTPUT"].update(str(e))

if __name__ == "__main__":
    main()
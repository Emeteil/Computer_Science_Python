import PySimpleGUI as sg

BITS = 4 * 1

degree = 2 ** BITS
c_range = (-degree // 2, degree // 2 - 1)

def number_to_direct(num: int) -> str:
    if not (c_range[0] <= num <= c_range[1]):
        raise ValueError("number not in (-128, 127)")
    
    return bin(abs(num))[2:].zfill(BITS)

def number_to_return(num: int) -> str:
    if not (c_range[0] <= num <= c_range[1]):
        raise ValueError("number not in (-128, 127)")
    
    return bin(~num & degree)[2:].zfill(BITS)

def number_to_additional(num: int) -> str:
    if not (c_range[0] <= num <= c_range[1]):
        raise ValueError("number not in (-128, 127)")
    
    return bin(~(num & degree) + 1)[2 if num > 0 else 3:].zfill(BITS)

def binary_to_int(num: str, without_first_bit: bool = False) -> int:
    if any(i not in "01" for i in num):
        raise ValueError("number non-binary")
    
    if num[0] == '0' or without_first_bit: return int(num, 2)
    return -((~int(num, 2) & degree) + 1)
    
def convert_numbers(window, values) -> None:
    number = int(values["NUMBER"])

    direct_code: str = number_to_direct(number)
    return_code: str = number_to_return(number)
    additional_code: str = number_to_additional(number)
    
    window["DIRECT_CODE"].update(direct_code)
    window["DIRECT_CODE_INT"].update(binary_to_int(direct_code, True))

    if abs(number) > c_range[1]:
        window["DIRECT_CODE"].update(text_color = "red")
        window["DIRECT_CODE_INT"].update(text_color = "orange")
    window["DIRECT_CODE"].update(text_color = "#80bcef")
    window["DIRECT_CODE_INT"].update(text_color = "#80bcef")
    
    if number >= 0:
        window["RETURN_CODE"].update("")
        window["RETURN_CODE_INT"].update("")
        window["ADDITIONAL_CODE"].update("")
        window["ADDITIONAL_CODE_INT"].update("")
        window["OUTPUT"].update("")
        return

    window["RETURN_CODE"].update(return_code)
    window["RETURN_CODE_INT"].update(binary_to_int(return_code))
    
    window["ADDITIONAL_CODE"].update(additional_code)
    window["ADDITIONAL_CODE_INT"].update(binary_to_int(additional_code))
    window["OUTPUT"].update("")

def main():
    sg.theme("Dark Grey 15")
    layout = [
        [
            sg.Column(
                [
                    [sg.Image(source = "task_4.png", size = (275, 275))]
                ],
                element_justification = 'center',
                justification = 'center',
                vertical_alignment = 'top'
            ),
            sg.Column(
                [
                    [sg.Text("Число")],
                    [sg.InputText(default_text = "", size = (15, 1), key = "NUMBER")],
                    [sg.Text("Прямой код")],
                    [
                        sg.Input(default_text = "", readonly = True, size = (10, 1), key = "DIRECT_CODE"),
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
        ]
    ]

    window = sg.Window("Байт", layout, size = (500, 300))
    
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
from PySG_gif_support import *
import PySimpleGUI as sg

BITS = 8 * 1

DEGREE = 2 ** BITS
C_RANGE = (-DEGREE // 2, DEGREE // 2 - 1)

def number_to_direct(num: int) -> str:
    if not (C_RANGE[0] <= num <= C_RANGE[1]):
        raise ValueError(f"number not in {C_RANGE}")
    
    return bin(abs(num))[2:].zfill(BITS)

def number_to_return(num: int) -> str:
    if not (C_RANGE[0] <= num <= C_RANGE[1]):
        raise ValueError(f"number not in {C_RANGE}")
    
    return bin(~abs(num) & (DEGREE - 1))[2:].zfill(BITS)

def number_to_additional(num: int) -> str:
    if not (C_RANGE[0] <= num <= C_RANGE[1]):
        raise ValueError(f"number not in {C_RANGE}")
    
    return bin((~abs(num) & (DEGREE - 1)) + 1)[2:].zfill(BITS)

def binary_to_int(num: str, without_first_bit: bool = False) -> int:
    if any(i not in "01" for i in num):
        raise ValueError("number non-binary")
    
    if num[0] == '0' or without_first_bit: return int(num, 2)
    return -((~int(num, 2) & (DEGREE - 1)) + 1)
    
def convert_numbers(window, values) -> None:
    if not values["NUMBER"]:
        raise ValueError()
    
    number = int(values["NUMBER"])
    window["NUMBER"].update(text_color = "#80bcef")
    
    if not (C_RANGE[0] <= number <= C_RANGE[1]):
        raise ValueError()

    direct_code: str = number_to_direct(number)
    
    window["DIRECT_CODE"].update(direct_code)
    window["DIRECT_CODE_INT"].update(binary_to_int(direct_code, True))

    col: bool = abs(number) > C_RANGE[1]
    window["DIRECT_CODE"].update(text_color = "red" if col else "black")
    window["DIRECT_CODE_INT"].update(text_color = "orange" if col else "black")
    
    if number >= 0:
        window["RETURN_CODE"].update("")
        window["RETURN_CODE_INT"].update("")
        window["ADDITIONAL_CODE"].update("")
        window["ADDITIONAL_CODE_INT"].update("")
        return
    
    return_code: str = number_to_return(number)
    additional_code: str = number_to_additional(number)

    window["RETURN_CODE"].update(return_code)
    window["RETURN_CODE_INT"].update(binary_to_int(return_code))
    
    window["ADDITIONAL_CODE"].update(additional_code)
    window["ADDITIONAL_CODE_INT"].update(binary_to_int(additional_code))

def main():
    sg.theme("Dark Grey 12")
    layout = [
        [
            sg.Column(
                [
                    [sg.Image(size = (275, 275), key = "IMAGE")]
                ],
                element_justification = 'center',
                justification = 'center',
                vertical_alignment = 'top'
            ),
            sg.Column(
                [
                    [sg.Text("Число")],
                    [sg.InputText(default_text = "", enable_events = True, size = (15, 1), key = "NUMBER")],
                    [sg.Text("Прямой код")],
                    [
                        sg.InputText(default_text = "", text_color = "black", readonly = True, size = (10, 1), key = "DIRECT_CODE"),
                        sg.InputText(default_text = "", text_color = "black", readonly = True, size = (4, 1), key = "DIRECT_CODE_INT")
                    ],
                    [sg.Text("Обратный код")],
                    [
                        sg.InputText(default_text = "", text_color = "black", readonly = True, size = (10, 1), key = "RETURN_CODE"),
                        sg.InputText(default_text = "", text_color = "black", readonly = True, size = (4, 1), key = "RETURN_CODE_INT")
                    ],
                    [sg.Text("Дополнительный код")],
                    [
                        sg.InputText(default_text = "", text_color = "black", readonly = True, size = (10, 1), key = "ADDITIONAL_CODE"),
                        sg.InputText(default_text = "", text_color = "black", readonly = True, size = (4, 1), key = "ADDITIONAL_CODE_INT")
                    ]
                ],
                element_justification = 'center',
                justification = 'center',
            )
        ]
    ]

    window = sg.Window("Представления чисел", layout, size = (500, 300), icon = "task_4.ico", finalize = True)
    
    _, stop_event = start_gif_animation(window, "IMAGE", "task_4.gif")
    
    while True:
        event, values = window.read()
        try:
            match event:
                case "NUMBER":
                    convert_numbers(window, values)
                case sg.WIN_CLOSED: break
                case _: pass
        except ValueError as e:
            window["DIRECT_CODE"].update("")
            window["DIRECT_CODE_INT"].update("")
            window["RETURN_CODE"].update("")
            window["RETURN_CODE_INT"].update("")
            window["ADDITIONAL_CODE"].update("")
            window["ADDITIONAL_CODE_INT"].update("")
            window["NUMBER"].update(text_color = "red")
        except Exception as e:
            print(e)

    stop_gif_animation(stop_event)
    window.close()

if __name__ == "__main__":
    main()
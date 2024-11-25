import PySimpleGUI as sg

c_image = [[sg.Image("bio.png")]]
c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
           [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
           [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
           [sg.Button("Рассчитать", font="Arial 20")]]

layout = [
    [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
]

window = sg.Window("Калькулятор бактерий", layout)

while 1:

    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    micro = value["micro"]  #здесь хранится количество бактерий изначально
    count = value["count"]  #здесь хранится количество секунд для которых требуется рассчитать
    res = 0                 #здесь будет храниться результат


    x_0, N = map(int, (micro, count))
    k = 2
    b = 1
    
    res = int(k**N * x_0 + b * (k**N - 1 / k - 1)) + 1
    
    # # or
    # count_b = x_0
    # for i in range(N):
    #     count_b = k * count_b + b
    # res = count_b


    if event == "Рассчитать":
        window["res"].update(res)


window.close()


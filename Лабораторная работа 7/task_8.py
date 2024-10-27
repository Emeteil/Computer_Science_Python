import sys

examples = [
    "Спартак-Локомотив 2:2",
    "Real Madrid-Barcelona 3:1",
    "Real Madrid 1-Real Madrid 2 1:3",
    "Спартак-Локомотив 0:0"
]

def main():
    text = examples[int(sys.argv[1])]
    
    i = text.index(":")
    while text[i] != " " and i != 0:
        i -= 1

    if i == 0:
        print("Входные данные некоректны!")
        return
    
    teams = text[:i].split("-")
    scores = list(map(int, text[i+1:].split(":")))
    
    if scores[0] > scores[1]:
        print(teams[0])
    elif scores[0] < scores[1]:
        print(teams[1])
    else:
        print("Ничья")

if __name__ == "__main__":
    main()
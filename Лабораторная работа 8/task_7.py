import sys

examples = [
    "4276440013361511",
    "4276440013361512",
    "42761336512"
]

def main():
    card = list(map(int, examples[int(sys.argv[1])]))
    
    L = []
    for i, d in enumerate(card):
        if (i + 1) % 2 == 0:
            L.append(d)
        else:
            d = d * 2
            L.append(d - (9 if d > 9 else 0))
    
    if sum(L) % 10 == 0:
        print("Корректный номер")
    else:
        print("Некорректный номер")
    

if __name__ == "__main__":
    main()
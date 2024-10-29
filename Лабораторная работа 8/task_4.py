def input_list() -> list:
    L = []
    while True:
        number = input("Введите число: ")
        if not number: break
        abs_number = number[1:] if number[0] == "-" else number
        if not abs_number.isdigit(): continue
        L.append(int(number))
    
    return L

def main():
    L = input_list()
    
    avr = sum(L)/len(L)
    less = [i for i in L if i < avr]
    equals = [i for i in L if i == avr]
    more = [i for i in L if i > avr]
    
    print(F"Среднее арифметическое: {avr}")
    print(F"Меньше: {less}")
    if equals: print(F"Равно: {equals}")
    print(F"Больше: {more}")

if __name__ == "__main__":
    main()
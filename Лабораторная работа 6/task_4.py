def main():
    char = "\""
    space = " "
    n = int(input("Высота ёлочки: "))
    
    if n < 2:
        print("Данные некоректы!")
        return
    
    for i in range(n):
        print(space * (n - i - 1) + char * (1 + i*2))
    print(space * (n-1) + char)

if __name__ == "__main__":
    main()
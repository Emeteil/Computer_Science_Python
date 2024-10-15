def sum_d(a: int | str):
    return sum(int(i) for i in str(a))

def main():
    N = input("Ваш номер билета: ")
    
    if len(N) != 6:
        print("Некорректный билет")
        return
    
    if sum_d(N[:len(N)//2]) == sum_d(N[len(N)//2:]):
        print("Поздравляю! Ваш билет - счастливый")
        return
    
    print("Обычный билет")
            

if __name__ == "__main__":
    main()
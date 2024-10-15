def main():
    years = int(input("Сколько лет собаке? > "))
    
    if years < 0:
        print("Ошибка!")
        return
    
    if years <= 2:
        r = years * 10.5
    else:
        r = 10.5 * 2 + (years - 2) * 4
    
    print(f"Введенный вами год эквивалентен {r} человеческим")

if __name__ == "__main__":
    main()
def main():
    peoples = []
    while True:
        growth = int(input("Вес: "))
        if growth == 0 and len(peoples) >= 2:
            break
        if growth == 0 and len(peoples) < 2:
            print("Некого сравнивать")
            return
        if growth > 0:
            peoples.append(growth)
    
    print(F"Самый высокий человек с ростом: {max(peoples)}")
    print(f"Самый низкий человек с ростом: {min(peoples)}")

if __name__ == "__main__":
    main()
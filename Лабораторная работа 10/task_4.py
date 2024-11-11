def main():
    files = {
        'м': "file8.txt",
        'ж': "file7.txt"
    }
    
    while True:
        count = input("Количество: ")
        if count.isdecimal(): break
    count = int(count)
    
    while True:
        gender = input("м/ж: ")
        if gender in files: break
    
    with open(f"input/{files[gender]}", "r", encoding = "utf-8") as f:
        for _ in range(count):
            line = f.readline()
            if not line: break
            print(line.split()[0])

if __name__ == "__main__":
    main()
def main():
    files = [
        "file5.txt",
        "file6.txt"
    ]
    word = "Academy"
    
    for file in files:
        with open(f"input/{file}", "r", encoding = "utf-8") as f:
            for i, line in enumerate(f):
                index = line.find(word)
                if index == -1: continue
                print(f"Слово {word} есть в {file} в {i + 1} строке")

if __name__ == "__main__":
    main()
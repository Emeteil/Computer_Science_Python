import sys

examples = [
    "фразу перевернуть",
    "тайна раскрыта",
    "привет",
    "привет всем присутствующим"
]

def main():
    text = examples[int(sys.argv[1])]
    
    split_text = text.split()
    if len(split_text) != 2:
        print("Ошибка! Некорректное количество слов")
        return
    
    result_text = " ".join(split_text[::-1])
    print(result_text)
    
if __name__ == "__main__":
    main()
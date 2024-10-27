import sys

examples = [
    "Вечер за окном.\nЕще один деньпрожит.\nЖизнь скоротечна...",
    "Просто текст",
    "Как вишня расцвела!\nОна с конясогнала\nИ князя-гордеца."
]

def syllable_count(text: str) -> bool:
    vowel_letters = "аеёиоуыэюя"
    result = 0
    for i in text.lower():
        if i in vowel_letters: result += 1
    return result

def main():
    text = examples[int(sys.argv[1])]
    quantities = [5, 7, 5]
    
    split_text = text.split("\n")
    
    if len(split_text) != len(quantities):
        print("Не хайку. Должно быть 3 строки.")
        return
    
    if all(
        syllable_count(string) == quantities[i]
        for i, string in enumerate(split_text)
    ):
        print("Хайку!")
    else:
        print("Не хайку.")

if __name__ == "__main__":
    main()
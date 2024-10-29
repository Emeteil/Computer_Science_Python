def input_list() -> list:
    L = []
    while True:
        word = input("Введите слово: ")
        if not word: break
        L.append(word)
    
    return L

def clipping_word(word: str) -> str:
    if len(word) <= 10: return word
    return f"{word[0]}{len(word)-2}{word[-1]}"

def main():
    n = int(input("n: "))
    L = input_list()
    
    print("\n".join(map(clipping_word, L[:n])))

if __name__ == "__main__":
    main()
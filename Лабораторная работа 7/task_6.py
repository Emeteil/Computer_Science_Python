import sys

examples = [
    "wdor#",
    "hoell#",
    "shacnidw#",
    "hello"
]

def main():
    text = examples[int(sys.argv[1])]

    if text[-1] != "#":
        print("Ошибка! Отсутствует символ #")
        return

    result_text = list("" for _ in text[:-1])
    j = 0
    for i in range(len(result_text)):
        result_text[0 + j if i % 2 == 0 else -1 - j] = text[i]
        if i % 2 != 0: j += 1

    result_text = "".join(result_text)
    print(result_text)

if __name__ == "__main__":
    main()
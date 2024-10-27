import sys

examples = [
    "Фильм не плохой.",
    "Книга плохая!",
    "Еда не плоха, но могла бы быть лучше."
]

replace_dict = {
    "не плохой": "хороший",
    "не плоха": "хороша"
}

def main():
    text = examples[int(sys.argv[1])]
    
    result_text = text
    for i, j in replace_dict.items():
        result_text = result_text.replace(i, j)
    
    print(result_text)

if __name__ == "__main__":
    main()
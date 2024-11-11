def main():
    file = "file6.txt"
    char = 'e'
    
    with open(f"input/{file}", "r", encoding = "utf-8") as f:
        text = f.read()
    
    split_text = text.split()
    
    count_words_with_char = sum(
        1 for word in split_text
        if char in word.lower()
    )
    
    print(
        f"Буква {char} встречается в {file} в " +
        f"{(count_words_with_char / len(split_text)) * 100:.2f}% слов."
    )

if __name__ == "__main__":
    main()
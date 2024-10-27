def main():
    text = "Довольно распространённая ошибка ошибка это лишний повтор повтор слова слова Смешно не не правда ли Не нужно портить хор хоровод"

    split_text = text.split()
    
    result_split_text = [split_text[0]]
    for word in split_text[1:]:
        if word != result_split_text[-1]:
            result_split_text.append(word)
    
    result_text = " ".join(result_split_text)
    
    print(result_text)

if __name__ == "__main__":
    main()
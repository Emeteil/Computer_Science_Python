import random
import string

def dialog_window_bool(text: str) -> bool:
    while True:
        char = input(f"{text} (Y/N): ").lower()
        if char in ['y', 'n']: break
    return char == 'y'

def dialog_window_size(text: str) -> int:
    while True:
        number = input(f"{text}: ")
        if number.isdigit(): break
    return int(number)

def main():
    while True:
        length = dialog_window_size("Длина пароля")

        if length == 0:
            print("Данные введены неверно!")
            continue
        break
    
    while True:
        uppercase_letters = dialog_window_bool("Нужны ли заглавные буквы?")
        lowercase_letters = dialog_window_bool("Нужны ли строчные буквы?")
        digits = dialog_window_bool("Нужны ли цифры?")
        special_characters = dialog_window_bool("Нужны ли специальные символы?")

        if not any([
                uppercase_letters,
                lowercase_letters,
                digits,
                special_characters
            ]):
            print("Данные введены неверно!")
            continue
        break

    symbols = (
        (string.ascii_uppercase if uppercase_letters else "")+
        (string.ascii_lowercase if lowercase_letters else "")+
        (string.digits if digits else "")+
        (string.punctuation if special_characters else "")
    )
    
    password = "".join(
        random.choice(symbols) for _ in range(length)
    )
    
    print(f"Ваш пароль: {password}")

if __name__ == "__main__":
    main()
import os

input_folder = "edit"
output_folder = "edit"

def get_filename_user(text: str) -> str:
    while True:
        filename = input(f"{text}: ")
        if os.path.isfile(f"{input_folder}/{filename}"): break
    return filename

def decrypt(filename: str) -> None:
    with open(f"{input_folder}/{filename}", 'r', encoding='utf-8') as f:
        text = f.read()
        
    decrypt_text = ' '.join((word[::-1] for word in text.split()))
    
    print(decrypt_text)

def encrypt(filename: str) -> None:
    with open(f"{input_folder}/{filename}", 'r', encoding='utf-8') as f:
        text = f.read()
        
    encrypt_text = ' '.join((word[::-1] for word in text.split()))
    
    with open(f"{output_folder}/e_{filename}", 'w', encoding='utf-8') as f:
        f.write(encrypt_text)
    
    print(f"Файл зашифрован и сохранён в {output_folder}/{filename}")

def _print_to_rows(items: dict) -> None:
    print(*[f"{i + 1}) {r}" for i, r in enumerate(items)], sep="\n")

def main():
    actions = {
        "Расшифровать файл": decrypt,
        "Засшифровать файл": encrypt
    }
    _print_to_rows(actions)
    while True:
        index = int(input("Действие > "))
        list(actions.values())[index - 1](
            get_filename_user("Входной файл")
        )

if __name__ == "__main__":
    main()
import random

def game(a: int = 1, b: int = 10) -> None:
    secret = random.randint(a, b)
    
    print("Хорошо, я загадал число. Попробуй его отгадать")
    
    i = 1
    while True:
        num = int(input(f"Попытка №{i} > "))
        
        if num != secret:
            print(
                f"Нее, ты не угадал, это число "
                + ('больше' if num > secret else 'меньше')
                + " моего. Попробуй снова"
            )
            i += 1
            continue
        
        print("Поздравляю! Вы угадали!")
        break

def dialog_window() -> bool:
    while True:
        char = input("Хотите сыграть ещё? (Y/N): ").lower()
        if char in ['y', 'n']: break
    return char == 'y'

def main():
    while True:
        game()
        if not dialog_window(): break

if __name__ == "__main__":
    main()
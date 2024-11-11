def main():
    filename = "task_5.txt"
    
    while True:
        string = input("Строка: ")
        if string: break
    
    with open(f"edit/{filename}", 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        lines.insert(len(lines) // 2, f"{string}\n")
        f.seek(0)
        f.write(''.join(lines))

if __name__ == "__main__":
    main()
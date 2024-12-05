from beartype import beartype
import os

@beartype
def _dialog_window_bool(text: str) -> bool:
    while True:
        char = input(f"{text} (Y/N): ").lower()
        if char in "yn": break
    return char == 'y'

@beartype
def _dialog_window_size(text: str) -> int:
    while True:
        number = input(f"{text}: ")
        if number.isdigit(): break
    return int(number)

@beartype
def _dialog_window_filename_create(
        text: str,
        path: str,
        type: str,
        ignore_none: bool = False
    ) -> str | None:
    while True:
        filename = input(f"{text}: ")
        if not filename and ignore_none: return None
        for c in ";|*?'\"`[]()$<>{}^#\/%!":
            filename = filename.replace(c, "")
        filepath = os.path.join(path, filename[:244] + f".{type[:10]}")
        if os.path.isfile(filepath) and\
            _dialog_window_bool(f"Перезаписать файл {filepath}?"):
                break
        break
    return filepath

@beartype
def _dialog_window_filename_get(
        text: str,
        path: str,
        type: str,
        count_files: int = 5
    ) -> str | None:
    files = [f for f in os.listdir(path) if f.endswith(type)]
    total_files = len(files)
    
    if total_files == 0:
        print("Файлы не найдены.")
        return None
    
    current_page = 1
    total_pages = (total_files + count_files - 1) // count_files
    
    while True:
        start_index = (current_page - 1) * count_files
        end_index = start_index + count_files
        
        print(text)
        print(f"{'-' * 8}Page {current_page}/{total_pages}{'-' * 8}")
        print("0) << Предыдущая страница <<")
        
        page_files = files[start_index:end_index]
        
        for i, file in enumerate(page_files, start = 1):
            print(f"{i}) {file}")
        
        print(f"{len(page_files) + 1}) >> Следующая страница >>")
        
        try:
            index = int(input("Действие > "))
            if index == 0:
                current_page = (current_page - 1) \
                    if current_page != 1 else total_pages
                continue
            if index == (len(page_files) + 1):
                current_page = (current_page + 1) \
                    if current_page != total_pages else 1
                continue
            return os.path.join(path, page_files[index - 1])
        except (IndexError, ValueError):
            print("Введённые данные некоректны!")
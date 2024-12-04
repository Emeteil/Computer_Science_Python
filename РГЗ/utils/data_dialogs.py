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
def _dialog_window_filename_create(text: str, path: str, type: str) -> str:
    while True:
        filename = input(f"{text}: ")
        for c in ";|*?'\"`[]()$<>{}^#\/%!":
            filename = filename.replace(c, "")
        filepath = os.path.join(path, filename[:244] + f".{type[:10]}")
        if not os.path.isfile(filepath): break
    return filepath

@beartype
def _dialog_window_filename_get(text: str, path: str, type: str) -> str:
    print(text)
    # while True:
    #     filename = input(f"{text}: ")
    #     for c in ";|*?'\"`[]()$<>{}^#\/%!":
    #         filename = filename.replace(c, "")
    #     filepath = os.path.join(path, filename[:244] + f".{type[:10]}")
    #     if not os.path.isfile(filepath): break
    # return filepath
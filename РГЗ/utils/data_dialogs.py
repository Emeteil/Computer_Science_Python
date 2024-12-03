from beartype import beartype

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
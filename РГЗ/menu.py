from beartype import beartype
import threading
import pygame
import queue
import json
import os

from utils.game_functions import (
    _one_step,
    _n_step
)
from utils.data_dialogs import (
    _dialog_window_bool,
    _dialog_window_size,
    _dialog_window_filename_create,
    _dialog_window_filename_get
)

stop_event = threading.Event()

@beartype
def _print_to_rows(items: dict) -> None:
    print(*[f"{i + 1}) {r}" for i, r in enumerate(items)], sep="\n")

@beartype
def n_step_dialog(grid: list[list[bool]], delay: int = 100) -> None:
    N = int(input("Количество шагов: "))
    without_delay = _dialog_window_bool("Без задержки?")
    _n_step(
        grid = grid,
        n = N,
        delay = delay if not without_delay else 0
    )
    print(f"Пройдено {N} шагов!")

@beartype
def automated_game(grid: list[list[bool]]) -> None:
    stop = threading.Event()
    
    delay = 100
    
    def inner_thread_func() -> None:
        while not stop.is_set() and not stop_event.is_set():
            _one_step(grid)
            pygame.time.delay(delay)
    
    thread = threading.Thread(target = inner_thread_func)
    thread.start()
    
    def inner_stop() -> None:
        stop.set()
        
    def change_delay() -> None:
        nonlocal delay
        delay = int(input("Задержка в миллисекундах: "))
        print(f"Новая задержка: {delay} миллисекунд")
    
    local_actions = {
        "Остановить": (
            inner_stop,
            (),
            lambda: print("Процесс остановлен")
        ),
        "Изменить задержку": (
            change_delay,
            ()
        )
    }
    
    while not stop.is_set() and not stop_event.is_set():
        try:
            _print_to_rows(local_actions)
            index = int(input("Действие > "))
            if stop.is_set() or stop_event.is_set(): break
            
            func = list(local_actions.values())[index - 1]
            func[0](*func[1])
            if len(func) > 2: func[2]()
        except (IndexError, ValueError):
            print("Введённые данные некоректны!")

@beartype
def clear_grid(grid: list[list[bool]]):
    rows, cols = len(grid), len(grid[0])
    grid.clear()
    grid.extend([[False for _ in range(cols)] for _ in range(rows)])

@beartype
def save_grid(grid: list[list[bool]]):
    filepath = _dialog_window_filename_create(
        text = "Название сохранения",
        path = "saves",
        type = "json"
    )
    
    with open(filepath, "w", encoding = "utf-8") as f:
        json.dump(grid, f, indent = 4)
    
    print(f"Файл {filepath} сохранён!")

@beartype
def load_grid(grid: list[list[bool]]):
    filepath = _dialog_window_filename_get(
        text = "Выберите файл",
        path = "saves",
        type = "json"
    )
    
    with open(filepath, "w", encoding = "utf-8") as f:
        json.dump(grid, f, indent = 4)
    
    print(f"Файл {filepath} сохранён!")

@beartype
def change_size(resize_data_queue: queue.Queue) -> None:
    if not _dialog_window_bool("Сбросить поле и изменить размер?"):
        return
    
    rows: int = _dialog_window_size("Количество строк(по умолчанию 10)")
    if rows < 5: rows = 5
    
    cols: int = _dialog_window_size("Количество столбцов(по умолчанию 10)")
    if cols < 5: cols = 5
    
    cell_size: int = _dialog_window_size("Размер ячейки(по умолчанию 40)")
    if cell_size < 5: cell_size = 5
    
    margin: int = _dialog_window_size("Растояние между ячейками(по умолчанию 5)")
    
    resize_data_queue.put({'rows': rows, 'cols': cols, 'cell_size': cell_size, 'margin': margin})

@beartype
def main_menu(grid: list[list[bool]], resize_data_queue: queue.Queue) -> None:
    actions = {
        "Запустить симуляцию": (
            automated_game,
            (grid,)            
        ),
        "Один шаг": (
            _one_step,
            (grid,),
            lambda: print("Один шаг сделан")
        ),
        "N шагов": (
            n_step_dialog,
            (grid,)
        ),
        "Изменить размер поля": (
            change_size,
            (resize_data_queue,)
        ),
        "Отчистить": (
            clear_grid,
            (grid,)
        )
    }
    
    while not stop_event.is_set():
        try:
            _print_to_rows(actions)
            index = int(input("Действие > "))
            if stop_event.is_set(): break
            
            func = list(actions.values())[index - 1]
            func[0](*func[1])
            if len(func) > 2: func[2]()
        except (IndexError, ValueError):
            print("Введённые данные некоректны!")
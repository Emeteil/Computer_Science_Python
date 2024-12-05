from beartype import beartype, roar
import threading
import datetime
import pygame
import queue
import json
import os

from utils.game_functions import (
    _one_step,
    _n_step
)

# from utils.game_functions_multithreading import (
#     _one_step,
#     _n_step
# )

# Optimized algorithms: https://github.com/lightln2/LifeOhLife

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
def clear_grid(grid: list[list[bool]]) -> None:
    rows, cols = len(grid), len(grid[0])
    grid.clear()
    grid.extend([[False for _ in range(cols)] for _ in range(rows)])

@beartype
def save_grid(grid: list[list[bool]]):
    filepath = _dialog_window_filename_create(
        text = "Название сохранения(по умолчанию дата_время)",
        path = "saves",
        type = "json",
        ignore_none = True
    )
    if stop_event.is_set(): return
    
    if not filepath:
        now = datetime.datetime.now()
        filepath = os.path.join(
            "saves",
            now.strftime("%Y-%m-%d_%H-%M-%S") + ".json"
        )
    
    with open(filepath, "w", encoding = "utf-8") as f:
        json.dump(grid, f, indent = 4)
    
    print(f"Файл {filepath} сохранён!")

@beartype
def load_grid(
        resize_data_queue: queue.Queue,
        cell_size: int,
        margin: int
    ) -> None:
    filepath = _dialog_window_filename_get(
        text = "Выберите файл",
        path = "saves",
        type = "json",
        count_files = 5
    )
    if stop_event.is_set(): return
    
    if not filepath: return
    
    @beartype
    def __check_grid_structure(grid: list[list[bool]]) -> None: pass
    
    try:
        with open(filepath, "r", encoding = "utf-8") as f:
            new_grid = json.load(f)
    except json.JSONDecodeError:
        print("Файл повреждён!")
        return
    
    try:
        __check_grid_structure(new_grid)
    except roar.BeartypeCallException:
        print("Некоректная структура файал")
        return
    
    rows, cols = len(new_grid), len(new_grid[0])
    
    resize_data_queue.put(
        {'rows': rows, 'cols': cols, 'cell_size': cell_size, 'margin': margin, 'new_grid': new_grid}
    )
    
    print(f"Файл {filepath} сохранён!")

@beartype
def change_size(resize_data_queue: queue.Queue) -> None:
    if not _dialog_window_bool("Сбросить поле и изменить размер?"):
        return
    if stop_event.is_set(): return
    
    rows: int = _dialog_window_size("Количество ячеек в строке")
    if rows < 5: rows = 5
    if stop_event.is_set(): return
    
    cols: int = _dialog_window_size("Количество ячеек в столбце")
    if cols < 5: cols = 5
    if stop_event.is_set(): return
    
    cell_size: int = _dialog_window_size("Размер ячейки")
    if cell_size < 5: cell_size = 5
    if stop_event.is_set(): return
    
    margin: int = _dialog_window_size("Растояние между ячейками")
    if stop_event.is_set(): return
    
    resize_data_queue.put({'rows': rows, 'cols': cols, 'cell_size': cell_size, 'margin': margin})

@beartype
def main_menu(
        grid: list[list[bool]],
        resize_data_queue: queue.Queue,
        cell_size: int,
        margin: int
    ) -> None:
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
        "Сохранить поле": (
            save_grid,
            (grid,)
        ),
        "Загрузить поле": (
            load_grid,
            (resize_data_queue, cell_size, margin)
        ),
        "Отчистить": (
            clear_grid,
            (grid,)
        ),
        "Wiki(URL)": (
            os.system,
            ("start https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life",)
        ),
        "Прикольные конструкции(URL)": (
            os.system,
            ("start https://life.written.ru/game_of_life_review_by_gardner",)
        ),
        "GitHub(URL)": (
            os.system,
            ("start https://github.com/Emeteil/Computer_Science_Python/tree/main/%D0%A0%D0%93%D0%97",)
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
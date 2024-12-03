from beartype import beartype
import threading
import pygame

from utils.game_functions import (
    _one_step,
    _n_step
)

stop_event = threading.Event()

@beartype
def _print_to_rows(items: dict) -> None:
    print(*[f"{i + 1}) {r}" for i, r in enumerate(items)], sep="\n")

@beartype
def n_step_dialog(grid: list[list[bool]]) -> None:
    N = int(input("Количество шагов: "))
    _n_step(
        grid = grid,
        n = N,
        delay = 100
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
    
    while not stop_event.is_set() and not stop_event.is_set():
        try:
            _print_to_rows(local_actions)
            index = int(input("Действие > "))
            if stop_event.is_set(): break
            
            func = list(local_actions.values())[index - 1]
            func[0](*func[1])
            if len(func) > 2: func[2]()
        except (IndexError, ValueError):
            print("Введённые данные некоректны!")
        

@beartype
def main_menu(grid: list[list[bool]]) -> None:
    actions = {
        "Один шаг": (
            _one_step,
            (grid,),
            lambda: print("Один шаг сделан")
        ),
        "N шагов": (
            n_step_dialog,
            (grid,)
        ),
        "Запустить": (
            automated_game,
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
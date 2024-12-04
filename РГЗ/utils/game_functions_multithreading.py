from concurrent.futures import ThreadPoolExecutor
from beartype import beartype
from copy import deepcopy
import pygame
import time

@beartype
def _alive_count(grid: list[list[bool]], row: int, col: int) -> int:
    indexs = [
        (-1, -1), # левая верхняя
        (-1, 0), # верхняя
        (-1, 1), # правая верхняя
        (0, -1), # левая
        (0, 1), # правая
        (1, -1), # нижняя левая
        (1, 0), # нижняя
        (1, 1) # нижняя правая
    ]
    rows, cols = len(grid), len(grid[0])
    count = 0
    for y_i, x_i in indexs:
        y, x = row + y_i, col + x_i
        if 0 <= y < rows and 0 <= x < cols and grid[y][x]:
            count += 1
    return count

@beartype
def __one_step_part(
        grid: list[list[bool]],
        new_grid: list[list[bool]],
        start_row: int,
        end_row: int
    ) -> None:
    for y in range(start_row, end_row):
        for x in range(len(grid[0])):
            neighbors = _alive_count(new_grid, y, x)
            if new_grid[y][x]:
                grid[y][x] = neighbors == 2 or neighbors == 3
            else:
                grid[y][x] = neighbors == 3

@beartype
def _one_step(grid: list[list[bool]], num_threads: int = 4) -> None:
    rows = len(grid)
    new_grid = deepcopy(grid)
    
    rows_per_thread = rows // num_threads
    futures = []
    
    with ThreadPoolExecutor(max_workers = num_threads) as executor:
        for i in range(num_threads):
            start_row = i * rows_per_thread
            end_row = start_row + rows_per_thread if i < num_threads - 1 else rows
            futures.append(executor.submit(__one_step_part, grid, new_grid, start_row, end_row))

    for future in futures:
        future.result()

@beartype
def _n_step(grid: list[list[bool]], n: int, delay: int = 0) -> None:
    start_time = time.time()
    for _ in range(n):
        _one_step(grid)
        pygame.time.delay(delay)
    print(f"Время выполнения {time.time() - start_time}")
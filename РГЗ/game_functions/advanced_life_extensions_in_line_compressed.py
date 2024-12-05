from beartype import beartype
import numpy as np
import pygame
import time

@beartype
def _one_step(grid: list[list[bool]]) -> None:
    rows, cols = len(grid), len(grid[0])
    neighbor_count = [[0] * cols for _ in range(rows)]

    for y in range(rows):
        for x in range(cols):
            if grid[y][x]:
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        if dy == 0 and dx == 0:
                            continue
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < rows and 0 <= nx < cols:
                            neighbor_count[ny][nx] += 1

    for y in range(rows):
        for x in range(cols):
            if grid[y][x]:
                grid[y][x] = neighbor_count[y][x] in (2, 3)
            else:
                grid[y][x] = neighbor_count[y][x] == 3


@beartype
def _n_step(grid: list[list[bool]], n: int, delay: int = 0) -> None:
    start_time = time.time()
    for _ in range(n):
        _one_step(grid)
        pygame.time.delay(delay)
    if not delay:
        print(f"Время выполнения {time.time() - start_time}")
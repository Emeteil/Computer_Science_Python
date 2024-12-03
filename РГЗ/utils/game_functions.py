from beartype import beartype
import pygame

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
def _one_step(grid: list[list[bool]]) -> None:
    rows, cols = len(grid), len(grid[0])
    for y in range(rows):
        for x in range(cols):
            neighbors = _alive_count(grid, y, x)
            if grid[y][x]:
                grid[y][x] = neighbors in (2, 3)
            else:
                grid[y][x] = neighbors in (3,)

@beartype
def _n_step(grid: list[list[bool]], n: int, delay: int = 0) -> None:
    for _ in range(n):
        _one_step(grid)
        pygame.time.delay(delay)
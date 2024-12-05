from beartype import beartype
import pygame
import time

@beartype
def _one_step(grid: list[list[bool]]) -> None:
    rows, cols = len(grid), len(grid[0])
    new_grid = [[False] * cols for _ in range(rows)]
    
    for y in range(rows):
        for x in range(cols):
            alive_neighbors = 0
            for dy, dx in [
                    (-1, -1), # левая верхняя
                    (-1, 0), # верхняя
                    (-1, 1), # правая верхняя
                    (0, -1), # левая
                    (0, 1), # правая
                    (1, -1), # нижняя левая
                    (1, 0), # нижняя
                    (1, 1) # нижняя правая                
                ]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx]:
                    alive_neighbors += 1
            
            if grid[y][x]:
                new_grid[y][x] = alive_neighbors in (2, 3)
            else:
                new_grid[y][x] = alive_neighbors == 3
    
    for y in range(rows):
        for x in range(cols):
            grid[y][x] = new_grid[y][x]

@beartype
def _n_step(grid: list[list[bool]], n: int, delay: int = 0) -> None:
    start_time = time.time()
    for _ in range(n):
        _one_step(grid)
        pygame.time.delay(delay)
    if not delay:
        print(f"Время выполнения {time.time() - start_time}")
from beartype import beartype
import pygame

@beartype
def draw_grid(
        screen: pygame.Surface,
        grid: list[list[bool]],
        cell_size: int,
        margin: int,
        life_color: tuple[int, int, int],
        dead_color: tuple[int, int, int]
    ) -> None:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            color = life_color if grid[row][col] else dead_color
            pygame.draw.rect(
                screen,
                color,
                [
                    (margin + cell_size) * col + margin,
                    (margin + cell_size) * row + margin,
                    cell_size, cell_size
                ]
            )

@beartype
def get_cell_coords(
        pos: tuple[int, int],
        cell_size: int,
        margin: int
    ):
    col = pos[0] // (cell_size + margin)
    row = pos[1] // (cell_size + margin)
    return col, row

@beartype
def update_grid(
        grid: list[list[bool]],
        pos: tuple[int, int],
        cell_size: int,
        margin: int
    ) -> None:
    col, row = get_cell_coords(pos, cell_size, margin)
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        grid[row][col] = not grid[row][col]
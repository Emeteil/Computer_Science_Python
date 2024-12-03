from beartype import beartype
import threading
import pygame
import queue
import sys

from utils.update_paint import *
from menu import main_menu, stop_event

pygame.init()

LIFE_COLOR = (255, 255, 255)
DEAD_COLOR = (0, 0, 0)
MARGIN_COLOR = (10, 10, 10)

CELL_SIZE = 40
MARGIN = 5

ROWS = 10
COLS = 10

@beartype
def change_size_window(
        grid: list[list[bool]],
        rows: int,
        cols: int,
        cell_size: int,
        margin: int
    ) -> None:
    global screen, ROWS, COLS, CELL_SIZE, MARGIN
    ROWS, COLS, CELL_SIZE, MARGIN = rows, cols, cell_size, margin
    grid.clear()
    grid.extend([[False for _ in range(cols)] for _ in range(rows)])
    window_size = [
        (CELL_SIZE + MARGIN) * COLS + MARGIN,
        (CELL_SIZE + MARGIN) * ROWS + MARGIN
    ]
    screen = pygame.display.set_mode(window_size)
    print(1)

def main() -> None:
    grid = [[False for _ in range(COLS)] for _ in range(ROWS)]

    window_size = [
        (CELL_SIZE + MARGIN) * COLS + MARGIN,
        (CELL_SIZE + MARGIN) * ROWS + MARGIN
    ]

    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Life")
    
    resize_data_queue = queue.Queue()
    
    thread = threading.Thread(
        target = lambda: main_menu(
            grid = grid,
            resize_data_queue = resize_data_queue
        )
    )
    thread.start()
    
    mouse_button_down = False
    previous_cell = None
    
    running = True
    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # ЛКМ
                        mouse_button_down = True
                        current_cell = get_cell_coords(pygame.mouse.get_pos(), CELL_SIZE, MARGIN)
                        update_grid(grid, pygame.mouse.get_pos(), CELL_SIZE, MARGIN)
                        previous_cell = current_cell
                case pygame.MOUSEBUTTONUP:
                    if event.button == 1: # ЛКМ
                        mouse_button_down = False
                case pygame.MOUSEMOTION:
                    if mouse_button_down:
                        current_cell = get_cell_coords(pygame.mouse.get_pos(), CELL_SIZE, MARGIN)
                        if current_cell != previous_cell:
                            update_grid(grid, pygame.mouse.get_pos(), CELL_SIZE, MARGIN)
                            previous_cell = current_cell
                case pygame.QUIT:
                    stop_event.set()
                    running = False

        if not resize_data_queue.empty():
            change_size_window(**resize_data_queue.get(), grid = grid)
        
        screen.fill(MARGIN_COLOR)
        draw_grid(screen, grid, CELL_SIZE, MARGIN, LIFE_COLOR, DEAD_COLOR)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
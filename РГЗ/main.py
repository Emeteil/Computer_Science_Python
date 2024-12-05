from beartype import beartype
import threading
import pygame
import queue
import yaml
import sys
import os

from utils.update_paint import *
from menu import main_menu, stop_event

pygame.init()

with open("settings.yml", "r", encoding = "utf-8") as f:
    settings = yaml.load(f, yaml.FullLoader)

if not os.path.isdir("saves"):
    os.mkdir("saves")

LIFE_COLOR = tuple(settings["LIFE_COLOR"])
DEAD_COLOR = tuple(settings["DEAD_COLOR"])
MARGIN_COLOR = tuple(settings["MARGIN_COLOR"])

CELL_SIZE = settings["CELL_SIZE"]
MARGIN = settings["MARGIN"]

ROWS = settings["ROWS"]
COLS = settings["COLS"]

@beartype
def change_size_window(
        grid: list[list[bool]],
        rows: int,
        cols: int,
        cell_size: int,
        margin: int,
        new_grid: list[list[bool]] = None
    ) -> None:
    global screen, ROWS, COLS, CELL_SIZE, MARGIN
    ROWS, COLS, CELL_SIZE, MARGIN = rows, cols, cell_size, margin
    grid.clear()
    if new_grid:
        grid.extend(new_grid)
    else:
        grid.extend([[False for _ in range(cols)] for _ in range(rows)])
    
    window_size = [
        (CELL_SIZE + MARGIN) * COLS + MARGIN,
        (CELL_SIZE + MARGIN) * ROWS + MARGIN
    ]
    screen = pygame.display.set_mode(window_size)

def main() -> None:
    grid = [[False for _ in range(COLS)] for _ in range(ROWS)]

    window_size = [
        (CELL_SIZE + MARGIN) * COLS + MARGIN,
        (CELL_SIZE + MARGIN) * ROWS + MARGIN
    ]

    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption(f"{settings['name']} v{settings['version']}")
    
    icon = pygame.image.load('icon.ico')
    pygame.display.set_icon(icon)
    
    resize_data_queue = queue.Queue()
    
    thread = threading.Thread(
        target = lambda: main_menu(
            grid = grid,
            resize_data_queue = resize_data_queue,
            cell_size = CELL_SIZE,
            margin = MARGIN
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
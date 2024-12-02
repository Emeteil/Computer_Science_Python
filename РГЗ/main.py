import pygame
import sys

from utils.update_paint import *
from utils.game_functions import *

pygame.init()

LIFE_COLOR = (255, 255, 255)
DEAD_COLOR = (0, 0, 0)
MARGIN_COLOR = (10, 10, 10)

CELL_SIZE = 40
MARGIN = 5

ROWS = 10
COLS = 10

def main():
    grid = [[False for _ in range(COLS)] for _ in range(ROWS)]

    window_size = [(CELL_SIZE + MARGIN) * COLS + MARGIN,
                   (CELL_SIZE + MARGIN) * ROWS + MARGIN]

    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Life")

    running = True
    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.MOUSEBUTTONDOWN:
                    update_grid(grid, pygame.mouse.get_pos(), CELL_SIZE, MARGIN)
                case pygame.QUIT:
                    running = False

        screen.fill(MARGIN_COLOR)
        draw_grid(screen, grid, CELL_SIZE, MARGIN, LIFE_COLOR, DEAD_COLOR)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
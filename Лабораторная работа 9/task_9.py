from random import shuffle
import time
import sys

def print_game_matrix(matrix: list) -> None:
    prints = ['.', '.', '.', '*', 'X']
    for i in matrix:
        for j in i:
            print(prints[j], end = " ")
        print()

def animate_explosion(matrix: list, delay: float = 0.4) -> None:
    print_game_matrix(matrix)
    sys.stdout.write("\033[F" * len(matrix))
    for x in range(len(matrix)):
        time.sleep(delay)
        for _ in range(len(matrix[x])):
            print("💥", end="")
        print()

def _dialog_window_bool(text: str) -> bool:
    while True:
        char = input(f"{text} (Y/N): ").lower()
        if char in "yn": break
    return char == 'y'

def count_ships(matrix: list[list]) -> int:
    count = 0
    for i in matrix:
        for j in i:
            count += (j == 1)
    return count

def game(
        n: int = 4,
        m: int = 4,
        ships: int = 4,
        bombs: int = 1
    ) -> tuple[bool, int] :
    chips = [1] * ships + [2] * bombs + [0] * (n * m - ships - bombs)
    shuffle(chips)
    matrix = [chips[i:i + m] for i in range(0, n * m, m)]
    
    if '--debug' in sys.argv: print(matrix)
    
    shift = {
        0: 3,
        1: 4
    }
    
    print_game_matrix(matrix)
    
    attempts = 0
    while True:
        x, y = map(int, input("x y: ").split())
        x -= 1
        y -= 1
        
        if x >= n or y >= m:
            print("Нельзя стрелять за пределы поля")
            continue
        
        if matrix[x][y] in (3, 4):
            print("Вы уже стреляли по этим координатам")
            continue
        
        attempts += 1
        
        if matrix[x][y] == 2:
            animate_explosion(matrix)
            return (False, attempts)
        
        matrix[x][y] = shift[matrix[x][y]]
        
        if count_ships(matrix) == 0:
            print_game_matrix(matrix)
            return (True, attempts)
        
        print_game_matrix(matrix)

def main():
    while True:
        results = game()
        print(
            (
                "Поздравляю, вы победили🎉\n" +
                f"Было потрачено {results[1]} попыток!"
            )
            if results[0] else
            "Вы случайно попали в бомбу и всё взорвалось😞"
        )
        
        if not _dialog_window_bool("Сыграть ещё?"):
            break

if __name__ == "__main__":
    main()
import random

def find_M(n: int) -> int:
    return (n * (n**2 + 1)) // 2

def diagonal(matrix: list[list], side: bool = False) -> list:
    result = []
    
    N = len(matrix)
    for i in range(N):
        result.append(matrix[i][(N - 1) - i if side else i])
        
    return result

def vertical(matrix: list[list], i: int) -> list:
    result = []
    
    for j in range(len(matrix)):
        result.append(matrix[j][i])
        
    return result

def magic_cube_check(matrix: list[list]) -> bool:
    N = len(matrix)
    M = find_M(N)
    
    for i in range(N):
        if sum(matrix[i]) != M or sum(vertical(matrix, i)) != M:
            return False
    
    if sum(diagonal(matrix)) != M:
        return False
    
    if sum(diagonal(matrix, True)) != M:
        return False
    
    return True

def print_matrix(matrix: list[list]) -> None:
    for i in matrix:
        for j in i:
            print(j, end = " ")
        print()

def main():
    N = int(input("Размер квадрата: "))
    M = find_M(N)
    
    b1: bool = N % 2 != 0
    b2: bool = N % 4 == 0
    b3: bool = N % 2 == 0 and N % 4 != 0
    
    if not any((b1, b2, b3)):
        print("Для такого размера невозможно создать магический квадрат")
        return
    
    max_attempts = 25 * N
    
    while True:
        matrix = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N - 1):
            attempt = 0
            while attempt < max_attempts:
                matrix[i] = random.sample(range(1, N**2 + 1), N)

                if not sum(matrix[i]) == M: continue

                if not all(sum(diagonal(matrix, j)) < M for j in (False, True)):
                    attempt += 1
                    continue

                if not all(sum(vertical(matrix, j)) < M for j in range(N)):
                    attempt += 1
                    continue

                break
            
            if attempt == max_attempts: break
        else:
            for i in range(N):
                matrix[-1][i] = M - sum(vertical(matrix, i))
            
            if magic_cube_check(matrix): break
    
    print_matrix(matrix)
    
if __name__ == "__main__":
    main()
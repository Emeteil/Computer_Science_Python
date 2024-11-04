import sys

examples = [
"""5 5
0 1 0 0 0
1 0 0 1 0
0 0 0 0 1
1 1 1 0 0
0 0 0 0 0
3""",
"""4 4
1 1 1 1
1 0 0 1
1 1 1 1
1 0 1 0
2""",
"""3 6
0 0 1 1 1 1
1 1 1 0 0 1
0 0 1 1 0 0
2""",
"""5 5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
3""",
"""6 6
0 1 0 1 0 0
1 0 1 0 1 0
0 0 0 0 0 1
1 0 1 0 1 0
0 1 0 1 0 0
1 0 0 1 0 1
4""",
"""4 7
1 0 1 0 1 0 1
1 1 1 1 1 1 1
1 0 0 0 1 1 1
0 0 0 0 0 0 1
5""",
"""5 5
0 0 1 1 1
1 1 1 1 1
1 1 1 0 0
1 1 1 0 1
0 0 1 0 1
2""",
]

def print_matrix(matrix: list) -> None:
    for i in matrix:
        for j in i:
            print(j, end = " ")
        print()

def find_row(n: int, m: int, k: int, matrix: list[list]) -> int:
    for i in range(n):
        c = 0
        for j in range(m):
            if not matrix[i][j]: c += 1
            else: c = 0
            if c == k: return i
    
    return -1

def main():
    example = examples[int(sys.argv[1])].split("\n")
    
    n, m = map(int, example[0].split())
    matrix = [list(map(int, i.split())) for i in example[1:-1]]
    k = int(example[-1])
    
    print(f"Нужно посадить группу из {k} человек")
    print(f"Кинотеатр {n}x{m}:")
    print_matrix(matrix)
    
    index = find_row(n, m, k, matrix) + 1
    
    if not index:
        print("Нету подходящего ряда😞")
        return        
        
    print(f"Можно сесть в {index} ряду")

if __name__ == "__main__":
    main()
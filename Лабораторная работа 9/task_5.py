import sys

examples = [
"""3 4
11 12 13 14
21 22 23 24
31 32 33 34""",
"""2 3
5 6 7
8 9 10""",
"""4 2
1 2
3 4
5 6
7 8""",
"""3 3
1 2 3
4 5 6
7 8 9"""
]

def print_matrix(matrix: list[list]) -> None:
    for i in matrix:
        for j in i:
            print(j, end = " ")
        print()

def main():
    example = examples[int(sys.argv[1])].split("\n")
    
    n, m = map(int, example[0].split())
    matrix = [list(map(int, i.split())) for i in example[1:]]
    
    print("Оригинал:")
    print_matrix(matrix)
    
    # T_matrix = list(zip(*matrix)) # list[tuple]
    # T_matrix = list(map(list, zip(*matrix))) # list[list]
    T_matrix = [list(i) for i in zip(*matrix)] # list[list]
    
    print("Транспонированная матрица:")
    print_matrix(T_matrix)

if __name__ == "__main__":
    main()
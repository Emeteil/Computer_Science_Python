import sys

examples = [
"""3
1 2 3
4 5 6
7 8 9""",

"""4
10 20 30 40
50 60 70 80
90 100 110 120
130 140 150 160""",

"""5
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5""",

"""6
6 7 8 9 10 11
12 13 14 15 16 17
18 19 20 21 22 23
24 25 26 27 28 29
30 31 32 33 34 35
36 37 38 39 40 41"""
]

def print_matrix(matrix: list[list]) -> None:
    for i in matrix:
        for j in i:
            print(j, end = " ")
        print()

def main():
    example = examples[int(sys.argv[1])].split("\n")
    
    n = int(example[0])
    matrix = [list(map(int, i.split())) for i in example[1:]]
    
    print("Оригинал:")
    print_matrix(matrix)
    
    for i in range(n):
        matrix[i][i], matrix[-1 - i][i] = matrix[-1 - i][i], matrix[i][i]
    
    print("Новая:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()
def print_matrix(matrix: list) -> None:
    for i in matrix:
        for j in i:
            print(j, end = " ")
        print()

def main():
    n, m = map(int, input("n m: ").split())
    
    matrix = [
        [1 for _ in range(m)]
        if not i else
        [1, *(0 for _ in range(m - 1))]
        for i in range(n)
    ]
    
    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    
    print_matrix(matrix)

if __name__ == "__main__":
    main()

# # Альтернатива
# matrix = [[] for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         if i == 0:
#             matrix[i].append(1)
#             continue
#         if j == 0:
#             matrix[i].append(1)
#             continue
#         matrix[i].append(matrix[i-1][j] + matrix[i][j-1])
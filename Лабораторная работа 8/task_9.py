import sys

examples = [
"""3
1 1
2 2
3 3""",
"""3
1 10
0 10
10 10""",
]

def main():
    example = examples[int(sys.argv[1])].split("\n")
    
    n = int(example[0])
    L = [tuple(map(int, i.split())) for i in example[1:]]
    
    rooms = 0
    for i in range(n):
        if L[i][1] - L[i][0] >= 2:
            rooms += 1

    print(rooms)

if __name__ == "__main__":
    main()
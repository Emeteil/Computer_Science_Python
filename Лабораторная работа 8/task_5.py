import sys

examples = [
    (
        176,
        [215, 207, 196, 176, 168, 166]
    ),
    (
        176,
        [215, 210, 207]
    ),
    (
        176,
        [215, 210, 207, 176, 176, 176, 176]
    )
]

def main():
    example = examples[int(sys.argv[1])]
    
    L = example[1]
    A = example[0]
    
    L.append(A)
    
    L.sort(reverse = True)
    
    index = len(L) - L[::-1].index(A)
    
    print(f"Андрей {index} по счёту")

if __name__ == "__main__":
    main()
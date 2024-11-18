import sys

letters = {
    1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

def main():
    score_dir = {}
    
    for k, v in letters.items():
        for c in v:
            score_dir[c.lower()] = k
    
    string: str = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "Hello"
    ).lower()
    
    print(f"Слово: {string.capitalize()}")
    
    score = sum(score_dir.get(c, 0) for c in string)
        
    print(f"Очков: {score}")

if __name__ == "__main__":
    main()
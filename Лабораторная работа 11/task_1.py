import sys

letters = {
    "0": [" "],
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"]
}

def main():
    replace_dir = {}
    
    for k, v in letters.items():
        for i, c in enumerate(v):
            replace_dir[c.lower()] = k * (i + 1)

    string: str = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "Hello World!"
    ).lower()
    new_string = string
    
    for c, d in replace_dir.items():
        new_string = new_string.replace(c, d)
        
    print(new_string)

if __name__ == "__main__":
    main()
import sys

examples = [
"""
4
QQAA
""".strip(),
"""
4
QQAQ
""".strip(),
"""
3
QAA
""".strip(),
"""
999
QQQQQQQQQQQQQQQAQAQ
""".strip()
]

def is_valid(N: int, chars: str) -> bool:
    chars = chars[1:N]
    
    if chars[0] != "Q":
        return False
    
    chars: list = [chars[0]] + [
        chars[i]
        for i in range(1, len(chars))
        if chars[i] != chars[i - 1]
    ]
    
    return chars.count("A") >= chars.count("Q")

def main():
    string = examples[int(sys.argv[1])]
    
    N, chars = string.split()
    N = int(N)
    
    print("+" if is_valid(N, chars) else "-")

if __name__ == "__main__":
    main()
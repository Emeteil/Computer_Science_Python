import sys

examples = [
    "Python",
    "",
    "h",
    "hello world"
]

def main():
    text = examples[int(sys.argv[1])]
    
    result_text = ".".join(text)
    print(result_text)

if __name__ == "__main__":
    main()
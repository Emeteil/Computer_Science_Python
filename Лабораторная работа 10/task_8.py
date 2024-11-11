empty = '.'
body = '#'

def main():
    while True:
        n = input("n: ")
        if n.isdecimal() and n != "0": break
    n = int(n)
    
    while True:
        m = input("m: ")
        if m.isdecimal() and m != "0": break
    m = int(m)
    
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(body * m)
            continue
        if i % 4 != 0:
            print(empty * (m - 1) + body)
        else:
            print(body + empty * (m - 1))

if __name__ == "__main__":
    main()
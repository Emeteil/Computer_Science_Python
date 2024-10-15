def main():
    bin_N = input("Двоичное число: ")
    
    if any(i not in ('0', '1') for i in bin_N):
        print("Число не в двоичной СС")
        return
    
    r = 0
    for i, j in enumerate(bin_N[::-1]):
        r += 2**i * int(j)

    print(r)

if __name__ == "__main__":
    main()
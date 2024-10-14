def main():
    n = int(input("n: "))
    result = sum(i**2 for i in range(1, n+1))
    print(result)

if __name__ == "__main__":
    main()
def main():
    with open("input/file4.txt", "r", encoding = "utf-8") as f:
        results = [
            (f"{name1} {name2}", int(score))
            for name1, name2, score in (
                i.split() for i in f
            )
        ]
    
    results.sort(reverse = True, key = lambda x: x[1])
    
    print(
        results[1][0] +
        f" (Набранное количество баллов: {results[1][1]})"
    )

if __name__ == "__main__":
    main()
def main():
    L = [
        1, "a", 3, 4, "b", 6
    ]
    
    numbers = [i for i in L if type(i) is int]
    letters = [i for i in L if type(i) is str]
    
    del L
    
    print(F"Числа: {numbers}")
    print(F"Буквы: {letters}")

if __name__ == "__main__":
    main()
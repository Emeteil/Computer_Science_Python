def main():
    L = [
        1, 5, 2, 4, 3
    ]
    
    new_L = [L[i] for i in range(1, len(L)) if L[i] > L[i-1]]
    
    print(f"Новый список: {new_L}")

if __name__ == "__main__":
    main()
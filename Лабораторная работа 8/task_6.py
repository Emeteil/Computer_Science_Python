import random

def main():
    L = []
    
    while True:
        L.append("Р" if random.randint(0, 1) else "О")

        print(L[-1], end = " ")
        if len(L) >= 3 and len(set(L[-3:])) == 1:
            print(f"(попыток: {len(L)})")
            return

if __name__ == "__main__":
    main()
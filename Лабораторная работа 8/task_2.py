import random

def main():
    ticket = random.sample(range(1, 50), 6)
    
    print(f"Билет: {ticket}")

if __name__ == "__main__":
    main()
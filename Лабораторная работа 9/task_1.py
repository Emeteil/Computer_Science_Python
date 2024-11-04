def integral(func, a: int | float, b: int | float, N: int = 10) -> float:
    h = (b - a) / N
    
    result = (h / 2) * (func(a) + func(b))
    result += h * sum(func(a + i * h) for i in range(1, N))
    
    return result

def main():
    F = lambda x: x**2 / (10 + x**3)
    
    for N in (10, 100, 1000000):
        print(f"Для N {N} интергал = {integral(F, -2, 5, N)}")

if __name__ == "__main__":
    main()
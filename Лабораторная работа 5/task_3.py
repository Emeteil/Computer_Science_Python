import math

def main():
	N = int(input("Введите число: "))

	len_N = int(math.log10(N)) + 1 if N != 0 else 1

	sum_d = 0
	for i in range(len_N):
		sum_d += ((N % 10**(i+1)) - (N % 10**i))//(10**i)

	print(f"Сумма: {sum_d}")

if __name__ == "__main__":
	main()
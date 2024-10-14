def main():
	N = int(input("Введите число N: "))
	K = int(input("Введите число K: "))

	R = N % 10**K
	print(R)

if __name__ == "__main__":
	main()
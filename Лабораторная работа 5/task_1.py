def main():
	S = input("Введите \"д:ч:м:с\" - ")
	
	L = list(map(int, S.split(":")))

	if len(L) > 4:
		print("Данные некоректны!")
		return

	k = [24*60*60, 60*60, 60, 1]

	sum_sec = 0
	for i in range(len(L)):
		sum_sec += L[i] * k[i + len(k)-len(L)]

	print(f"Общее количество секунд: {sum_sec}")

if __name__ == "__main__":
	main()
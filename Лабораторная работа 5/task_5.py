def main():
	A, B, C = map(int, input("Введите длины сторон через пробел: ").split())

	if A+B <= C:
		print("Тругольника не существует!")
		return

	if A == B == C:
		print("Равносторонний")
	elif A != B != C:
		print("Разносторонний")
	else:
		print("Равнобедренный")

if __name__ == "__main__":
	main()
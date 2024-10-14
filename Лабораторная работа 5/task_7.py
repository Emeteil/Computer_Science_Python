def main():
	N = input("Введите номер машины: ")

	if len(N) not in (6, 7):
		print("Такого формата нет!")
		return

	a: str = N[:3]
	b: str = N[3:]

	if not (a.isupper() and not a.isdigit()):
		print("Такого формата нет!")
		return

	if len(b) == 4:
		print("Формат новый")
		return

	print("Формат старый")

if __name__ == "__main__":
	main()
def main():
	N = input("Введите месяц: ").strip().lower()

	months = {
		"январь": 31,
		"февраль": (28, 29),
		"март": 31,
		"апрель": 30,
		"май": 31,
		"июнь": 30,
		"июль": 31,
		"август": 31,
		"сентябрь": 30,
		"октябрь": 31,
		"ноябрь": 30,
		"декабрь": 31
	}

	if N not in months:
		print("Данные некоректны!")
		return

	days = months[N]

	if type(days) is tuple:
		days_s = [str(i) for i in days]
		print(f"В этом месяце {' или '.join(days_s)} дней!")
		return

	print(f"В этом месяце {days} дней!")

if __name__ == "__main__":
	main()
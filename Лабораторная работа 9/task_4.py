menu = [
    ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
    ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
    ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]

col = {
    "red": "\033[31m",
    "yellow": "\033[33m",
    "green": "\033[32m",
    "r": "\033[0m"
}

def _print_dish(dish: list, leaght: int = 60) -> None:
    dots = '.' * (leaght - len(dish[0]) - 11 - len(str(dish[2])))
    print(f"{col['yellow']}{dish[0]} {dots} {dish[2]} попугаев{col['r']}")
    print(f"{col['green']}Ингредиенты: {', '.join(dish[1])}{col['r']}")

def print_menu(leaght: int = 60) -> None:
    print("Меню ресторана \"Вкусно и быстро\":")
    for i in range(len(menu)):
        _print_dish(menu[i], leaght)
        if i != len(menu) - 1: print()

def _dialog_window_bool(text: str) -> bool:
    while True:
        char = input(f"{text} (Y/N): ").lower()
        if char in "yn": break
    return char == 'y'

def _search_in_menu(string: str) -> int:
    for i in range(len(menu)):
        if menu[i][0].lower() == string.lower():
            return i
    else: return -1

def search() -> None:
    print("Что вы хотите найти?🔍")
    while True:
        string = input("Поиск: ")
        index = _search_in_menu(string)
        if index == -1:
            print("Похоже такого блюда нету😞")
            if _dialog_window_bool("Поискать снова?"):
                continue
            else: break
        _print_dish(menu[index])
        break

def add_dish() -> None:
    global menu
    title = input("Название блюда: ")
    
    ingredients = set()
    print("Ингридиенты:")
    while True:
        ingredient = input()
        if not ingredient: break
        ingredients.add(ingredient.lower())
    
    while True:
        price = input("Цена: ")
        if price.isdigit(): break
    price = int(price)
    
    menu.append([
        title,
        list(ingredients),
        price
    ])

def change_price() -> None:
    global menu
    print("Цену какого товара вы хотите изменить?🔍")
    while True:
        string = input("Поиск: ")
        index = _search_in_menu(string)
        
        if index == -1:
            print("Похоже такого блюда нету😞")
            if _dialog_window_bool("Поискать снова?"):
                continue
            else: break
        
        _print_dish(menu[index])
        
        while True:
            new_price = input("Новая цена: ")
            if new_price.isdigit(): break
        new_price = int(new_price)
        
        menu[index][2] = new_price
        print(f"Цена обновлена на {new_price} попугаев")
        break

def _print_to_rows(items: dict) -> None:
    print(*[f"{i + 1}) {r}" for i, r in enumerate(items)], sep="\n")

def main():
    actions = {
        "Отобразить меню ресторана": print_menu,
        "Найти блюдо по названию и отобразить его ингредиенты и цену": search,
        "Добавить новое блюдо в меню": add_dish,
        "Изменить цену блюда": change_price,
        "Выход": exit
    }
    _print_to_rows(actions)
    while True:
        index = int(input("Действие > "))
        list(actions.values())[index - 1]()

if __name__ == "__main__":
    main()
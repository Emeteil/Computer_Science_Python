def distance(
        point1: tuple[int | float, int | float],
        point2: tuple[int | float, int | float]
    ) -> float:
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2) ** 0.5

def main():
    treasure_map = []
    
    n = int(input("Количество сокровищ: "))
    
    print("Координаты сокровищ:")
    for _ in range(n):
        while True:
            coordinates = list(map(int, input().split()))
            if len(coordinates) == 2: break
        treasure_map.append(coordinates)
    
    while True:
        coordinates_alexandra = list(
            map(int, input("Координаты Александра: ").split())
        )

        if len(coordinates) == 2: break
    
    treasure_map_distances = []
    
    for coordinate in treasure_map:
        treasure_map_distances.append((
            distance(
                coordinate,
                coordinates_alexandra
            ),
            coordinate
        ))
    
    closest_treasures = min(treasure_map_distances, key = lambda x: x[0])
    print(f"Ближайшие сокровища: {closest_treasures[1]}")

if __name__ == "__main__":
    main()
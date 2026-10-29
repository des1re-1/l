parts = input("Введите целые числа через пробел: ").split()

if not parts:
    print("Нет данных")
else:
    numbers = [int(part) for part in parts]
    max_value = max(numbers)

    indices = []
    for i, value in enumerate(numbers):
        if value == max_value:
            indices.append(i)

    print(indices)
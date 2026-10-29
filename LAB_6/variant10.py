parts = input("Введите целые числа через пробел: ").split()
numbers = [int(part) for part in parts]

selected = []

for number in numbers:
    if number >= 10:
        selected.append(number)

sorted_copy = sorted(selected)

print(f"Выборка: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Отсортированная копия: {sorted_copy}")
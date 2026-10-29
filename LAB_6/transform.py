parts = input("Введите целые числа через пробел: ").split()
numbers = [int(part) for part in parts]

transformed = []
for number in numbers:
    if number < 0:
        transformed.append(abs(number))
    else:
        transformed.append(number)

print(f"Исходный список: {numbers}")
print(f"Новый список: {transformed}")
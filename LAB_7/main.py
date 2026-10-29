from functions import sum_digits, average, normalize_text, select_numbers


def main():
    # 1) Целое число
    number = int(input("Введите целое число: "))
    print(f"Сумма цифр: {sum_digits(number)}")

    # 2) Строка чисел
    parts = input("Введите числа через пробел: ").split()
    numbers = [int(part) for part in parts]

    avg = average(numbers)
    if avg is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {avg}")

    # 3) Произвольный текст
    text = input("Введите текст: ")
    print(f"Нормализованный текст: {normalize_text(text)}")

    # 4) Индивидуальный вариант (вариант 1)
    threshold = int(input("Введите порог (целое неотрицательное): "))
    selected = select_numbers(numbers, threshold)
    print(f"Выборка по условию: {selected}")


if __name__ == "__main__":
    main()
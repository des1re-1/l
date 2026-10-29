def sum_digits(number):
    """Вернуть сумму цифр модуля целого числа."""
    number = abs(number)

    if number == 0:
        return 0

    total = 0
    while number > 0:
        total += number % 10
        number //= 10

    return total


def average(numbers):
    """Вернуть среднее списка чисел или None для пустого списка."""
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Нижний регистр, убрать пробелы по краям, внутри оставить по одному пробелу."""
    return " ".join(text.lower().split())

def select_numbers(numbers, threshold):
    result = []
    for number in numbers:
        if -threshold <= number <= 0:
            result.append(number)
    return result
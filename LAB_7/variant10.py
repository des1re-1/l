def select_numbers(numbers, threshold):
    """
    Вариант 10: выбрать числа от -threshold до 0 включительно.
    """
    result = []
    for number in numbers:
        if -threshold <= number <= 0:
            result.append(number)
    return result
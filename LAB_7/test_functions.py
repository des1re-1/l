from functions import average, normalize_text, sum_digits, select_numbers

# Базовые проверки
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12

assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9

assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# Проверки варианта 10
base = [-5, 0, 2, 5]
threshold = 2
assert select_numbers(base, threshold) == [0]   # по таблице

# Пустой список
assert select_numbers([], 2) == []

# Границы и рядом с ними:
# включаются -threshold и 0, не включаются меньше -threshold и больше 0
assert select_numbers([-3, -2, -1, 0, 1], 2) == [-2, -1, 0]

# threshold = 0 -> только 0
assert select_numbers([-1, 0, 1], 0) == [0]

# Повторы сохраняются
assert select_numbers([0, -2, 0, -2, 1], 2) == [0, -2, 0, -2]

# Исходный список не меняется
numbers = [-5, 0, 2, 5]
copy_before = numbers.copy()
_ = select_numbers(numbers, 2)
assert numbers == copy_before

print("Базовые и вариантные проверки пройдены")
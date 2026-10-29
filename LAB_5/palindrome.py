text = input("Введите текст: ")

# Игнорируем регистр и обычные пробелы " "
cleaned = text.lower().replace(" ", "")

if cleaned == "":
    print("Нет текста")
else:
    if cleaned == cleaned[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")
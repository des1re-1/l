text = input("Введите строку: ")

words = text.split()
result = []

for word in words:
    cleaned = word.strip(".,!?;:").lower()
    if cleaned == "":
        continue

    if cleaned.startswith(cleaned[-1]):
        result.append(cleaned)

if result:
    for w in result:
        print(w)
else:
    print("Нет совпадений")

print(f"Количество: {len(result)}")
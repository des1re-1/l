print("1 - сложение")
print("2 - вычитание")
print("3 - умножение")
print("4 - деление")

a=float(input("Введите первое число:"))
b=float(input("Введите второе число:"))
c=int(input("Выберите действие:"))

if c== 1:
    print(a+b)
elif c== 2:
    print(a-b)
elif c== 3:
    print(a*b)
elif c== 4 and b!=0:
    print(a/b)
else:
    print('Неделимое')
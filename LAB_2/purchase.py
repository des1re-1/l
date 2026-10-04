price=int(input('Введите цену одной тетради:'))
count=int(input('Введите количество тетрадей:'))
paid=int(input('Введите внесенную сумму:'))
print('Стоимость тетрадей:'+str(count*price)+'. Сдача:'+str(paid-count*price)+'.')
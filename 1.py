import datetime

start = datetime.datetime.now()
sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
print(datetime.datetime.now() - start)
''' Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9.
Сумма этих чисел равна 23. Найдите сумму всех чисел меньше 1000, кратных 3 или 5. '''

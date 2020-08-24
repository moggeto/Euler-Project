import datetime

start = datetime.datetime.now()
s = []
f = 0
feb_1 = 1
feb_2 = 1
s.append(feb_1)
for i in range(2, 100):
    feb_1, feb_2 = feb_2, feb_1 + feb_2
    s.append(feb_1)
    if feb_1 >= 4000000:
        break
for j in s:
    if j % 2 == 0:
        f += j
print(f)
print(datetime.datetime.now() - start)
'''
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.'''

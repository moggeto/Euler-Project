import datetime

start = datetime.datetime.now()
n = 2 ** 10000
s = 0
while n > 0:
    digit = n % 10
    s = s + digit
    n = n // 10
print(s)
print(datetime.datetime.now() - start)
'''
2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2^1000?
'''
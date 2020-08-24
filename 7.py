import datetime

start = datetime.datetime.now()
n = 130000
numbers = list(range(2, n + 1))
for number in numbers:
    if number != 0:
        for candidate in range(2 * number, n+1, number):
            numbers[candidate-2] = 0
a = sorted(list(set(numbers)))
a.remove(0)
print(a[10000])
print(datetime.datetime.now() - start)
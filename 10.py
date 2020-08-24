from datetime import datetime

start = datetime.now()
n = 2000000
numbers = list(range(2, n + 1))
for number in numbers:
    if number != 0:
        for candidate in range(2 * number, n+1, number):
            numbers[candidate-2] = 0

print(sum(numbers))
print(datetime.now() - start)
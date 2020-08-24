from datetime import datetime

start = datetime.now()
lenage = {}
counter = []
for i in range(500000, 1000000):
    b = i
    while i != 1:
        if i % 2 == 0:
            i = i / 2
        else:
            i = (3 * i) + 1
        counter.append(i)
    a = len(counter)
    lenage[b] = a
    counter.clear()
print(max(lenage, key=lambda key: lenage[key]))
print(datetime.now() - start)
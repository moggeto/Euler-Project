import datetime

start = datetime.datetime.now()
s = []
for i in range(100, 1000):
    for j in range(100, 1000):
        b = i * j
        a = str(b)
        if a == a[::-1]:
            s.append(b)
s.sort()
print(s[-1])
print(datetime.datetime.now() - start)
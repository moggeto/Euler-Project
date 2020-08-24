import datetime

start = datetime.datetime.now()

s = []
c = []


def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def Factor(n):
    Ans = []
    d = 2
    while d <= n:
        if n % d == 0:
            Ans.append(d)
            n = n // d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans


for i in Factor(600851475143):
    s.append(i)
    a = 600851475143 / i
    s.append(a)
for i in s:
    if IsPrime(i) != 0:
        c.append(i)
print(max(c))
print(datetime.datetime.now() - start)
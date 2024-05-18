def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b.replace('0', '11')
    else:
        b = b.replace('1', '10')
    return int(b, 2)


print(f(12))
print(f(5))

res = []
for r in range(1, 100_000):
    if f(r) <= 161:
        res.append(f(r))
print(max(res))

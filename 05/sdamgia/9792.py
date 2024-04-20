def f(n):
    a = [int(r) for r in list(str(n))]
    b = a[0] * a[1]
    c = a[1] * a[2]
    res = sorted([b, c])
    return "".join(map(str, res))


res = []
for r in range(100, 1000):
    if f(r) == "621": res.append(r)
print(max(res))

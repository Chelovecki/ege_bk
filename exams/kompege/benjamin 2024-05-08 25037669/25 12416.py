from fnmatch import fnmatch


def div(n):
    res = set()
    for r in range(1, int(n ** 0.5) + 1):
        if n % r == 0:
            res.add(r)
            res.add(n // r)
    return (min(res) + max(res)) % 2 == 1


a = [r for r in range(125_670, 10 ** 10) if fnmatch(str(r), '12*567?')]
print(a)
print()
print()
b = [r for r in a if r % 7777 == 0]
print(b)
print()
print()
c = [r for r in b if div(r)]
print(c)

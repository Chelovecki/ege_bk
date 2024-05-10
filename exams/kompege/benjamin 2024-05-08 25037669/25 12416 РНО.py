from fnmatch import fnmatch


def div(n):
    res = set()
    for r in range(1, int(n ** 0.5) + 1):
        if n % r == 0:
            res.add(r)
            res.add(n // r)
    return (min(res) + max(res)) % 2 == 1


for r in range(7777, 10 ** 10, 7777):
    if fnmatch(str(r), '12*567?'):
        if div(r):
            print(r, r // 7777)

print("--------------")
for r in range(7777, 10 ** 10, 7777):
    if fnmatch(str(r), '12*567?'):
        if r % 2 == 0:
            print(r, r // 7777)

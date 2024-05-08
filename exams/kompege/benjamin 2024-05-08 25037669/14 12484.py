def to_5(n):
    res = ''
    while n != 0:
        res += str(n % 5)
        n //= 5
    return res


res = []
a = range(10000)
for x in a:
    for y in a:
        num = (5 ** 50) + (5 ** 30) - (5 ** x) - y - (5 ** y) - x
        if num > 0 and to_5(num).count('0') == 10:
            res.append(x * y)
            print(x * y)
print(max(res))

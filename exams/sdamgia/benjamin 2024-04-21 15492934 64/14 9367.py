def to_3(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res


print(to_3(9 ** 8 + 3 ** 5 - 9).count('2'))

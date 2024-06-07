def to_7(n):
    res = ''
    while n != 0:
        res += str(n % 7)
        n //= 7
    return res[::-1]

n = 7**21 + 49**13 - 7**10

print(to_7(n).count('6'))
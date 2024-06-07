def to5(n):
    res = ''
    while n != 0:
        res += str(n % 5)
        n //= 5
    return res[::-1]

n = 7*5**123 + 6*5**111 - 5*25**50 + 4*125**30 - 3*5**10

res = to5(n)

print(res.count('4'))
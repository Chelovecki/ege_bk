def to_7(n):
    res = ''
    while n != 0:
        res += str(n % 7)
        n //= 7
    return res[::-1]

n = 3*7**82 - 4*49**21 + 5*343**25

print(sum(int(r) for r in to_7(n)))

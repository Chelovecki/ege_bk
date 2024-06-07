n = 2 ** 2048 + 32 ** 102 - 8 * 4 ** 128
c = 0
while n != 0:
    div = n % 32
    if div > 9:
        c += 1
    n //= 32
print(c)

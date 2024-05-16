n = (2 * 729 ** 2014) + (2 * 81 ** 2018) + (2 * 27 ** 2020) - (2 * 9 ** 2022) - 2024

res = ''
while n != 0:
    a = n % 27
    if a > 9:
        res += '*'
    else:
        res += str(a)
    n //= 27

print(res.count('*'))

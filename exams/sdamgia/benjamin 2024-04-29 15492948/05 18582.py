def f(n):
    b = bin(n)[2:]
    while b[0] == '0': b = b[1:]
    if b.count('1') > b.count('0'):
        b += '1'
    elif b.count('0') >= b.count('1'):
        b += '0'

    return int(b,2)

print(f(13))


for r in range(1,1000):
    a = f(r)
    if a > 100:
        print(a)
        break

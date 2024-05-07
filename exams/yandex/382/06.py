def f(n):
    b = bin(n)[2:].zfill(8)
    new_b = ''
    for symb in b:
        if symb == '1':
            new_b += '0'
        else:
            new_b += '1'
    return int(new_b, 2) - n


# print(f(80))

for r in range(100000):
    if f(r) == 153:
        print(r)
        break
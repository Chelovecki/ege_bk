def f(n):
    b = bin(n)[2:].zfill(8)
    new_b = ''
    for r in b:
        if r == '1':
            new_b += '0'
        else:
            new_b += '1'
    return int(new_b, 2) - n


print(f(13) == 229)

for r in range(256):
    if f(r) == 111:
        print(r)
        break

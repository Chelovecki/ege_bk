def f(n):
    b = bin(n)[2:]

    b += str(sum(int(r) for r in b) % 2)
    b += str(sum(int(r) for r in b) % 2)
    return int(b, 2)


print(f(13))

for r in range(1, 1000):
    if f(r) > 154:
        print(r)
        break

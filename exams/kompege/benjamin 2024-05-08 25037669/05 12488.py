def f(n):
    b = bin(n)[2:]
    s = sum(map(int, list(b)))
    if s % 2 == 0:
        b += '0'
        b = '1' + '1' + b[2:]
    else:
        b += '1'
        b = '1' + '0' + b[2:]
    return int(b, 2)


print("проверка: ")
print(f(6))
print(f(4))

print("\nответ: ")
res = []
for r in range(50):
    res.append(f(r))
print(max(res))

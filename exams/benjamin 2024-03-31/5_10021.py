def f(n: int):
    bin_n = bin(n)[2:]
    new_bin = ''
    if bin_n.count('0') > bin_n.count('1'):
        for r in bin_n:
            if r == '1':
                new_bin += '0'
            else:
                new_bin += '1'

    elif bin_n.count('0') <= bin_n.count('1'):
        for num, r in enumerate(bin_n):
            if num % 2 == 0:
                new_bin += '1'
            else:
                new_bin += r

    return int(new_bin, 2)
res = []
for n in range(1,100000):
    if f(n) <= 1337:
        res.append((n,f(n)))

sorted_res = sorted(res, key=lambda x: x[1])
print(f"максимальное значение, не превышающее 1337: {sorted_res[-1][1]}")
print("значения n, которые выводят такой результат функции:")
for r in sorted_res:
    if r[1] == sorted_res[-1][1]:
        print(r)

print("минимальное значение n = 2760")

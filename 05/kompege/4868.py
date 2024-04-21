def f(n):
    chet_nums = sum([int(r) for r in str(n) if int(r) % 2 == 0])

    n = str(n)
    while n[0] == '0': n = n[1:]
    chet_spot = sum([int(n[idx]) for idx in range(len(n)) if (idx + 1) % 2 == 0])

    return abs(chet_nums - chet_spot)


print(f"проверка f(2021) = {f(2021)}")

for r in range(2, 2000):
    if f(r) == 13:
        print(r)
        break

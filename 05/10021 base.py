def f(n: int):
    bin_n = bin(n)[2:]
    new_bin = ''
    биты_на_четных_позициях = [bin_n[r] for r in range(len(bin_n)) if r%2==1]
    if биты_на_четных_позициях.count('0') > биты_на_четных_позициях.count('1'):
        for r in bin_n:
            if r == '1':
                new_bin += '0'
            else:
                new_bin += '1'

    elif биты_на_четных_позициях.count('0') <= биты_на_четных_позициях.count('1'):
        for num, r in enumerate(bin_n):
            if num % 2 == 0:
                new_bin += '1'
            else:
                new_bin += r

    return int(new_bin, 2)

res = {}
for n in range(1,100000):
    res_funk = f(n)
    if f(n) <= 1337:
        if res.get(res_funk):
            res[res_funk].append(n)
        else:
            res[res_funk] = []
            res[res_funk].append(n)

print(max(res.keys()))
print(res[max(res.keys())])
print("ответ:", min(res[max(res.keys())]))

# for key in sorted(list(res.keys())):
#     print(key, res[key])

# загвоздка заключается в том, что БИТЫ НУМЕРУЮТСЯ НАЧИНАЯ С ЕДИНИЦЫ БЛЯТЬ. не с нуля, как у всех нормальных людей,
# а с единицы

# 13099 кабанов
def f(start, end, contr):
    if start > end + 10000:
        return 0
    if start == end: return 1
    if contr == 'a':
        return f(start * 2, end, 'b') + f(start * 3, end, 'c')
    else:
        return f(start - 1, end, 'a') + f(start * 2, end, 'b') + f(start * 3, end, 'c')


print(f(3, 15, ''))

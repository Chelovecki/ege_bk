import itertools


def first_cond(number:int):
    res = ''
    while number!=0:
        res += str(number%7)
        number//=7
    res = res[::-1]
    while res[0] == "0":
        res = res[1:]
    return len(res) <= 7

def second_cond(number:int):
    last_digit = hex(number)[2:][-1]
    return last_digit == 'f'

def third_cond(number:int):
    res = ''
    while number != 0:
        res += str(number % 5)
        number //= 5
    res = res[::-1]
    while res[0] == "0":
        res = res[1:]
    s = set(res)
    q = [res.count(i) for i in s]
    count_nechet = sum([i % 2 for i in q])
    if len(res) % 2 == 0:
        return count_nechet == 0
    return count_nechet == 1

c = 0
for r in range(1,1_000_000):
    if third_cond(r) and first_cond(r) and second_cond(r):
        c+= 1
print(c)

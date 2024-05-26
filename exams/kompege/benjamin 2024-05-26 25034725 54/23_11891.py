from functools import lru_cache


@lru_cache(None)
def f(a, b):
    if a > b or a == 100: return 0
    if a == b: return 1

    log_a = a + (a % 10)
    log_b = a + (a % 68)
    log_c = a ** 2
    if log_a != a:
        print(a)
        res1 = f(log_a, b) #if log_a != a else 0
    else:
        return 0
    res2 = f(log_b, b) #if log_b != a else 0
    res3 = f(log_c, b) #if log_c != a else 0

    return res1 + res2 + res3


a = f(2, 68)
print("до 68")
b = f(68, 680)
print(a * b)

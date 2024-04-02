import math
from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if float(math.sqrt(n)) == int(math.sqrt(n)):
        return f(n - 1) - n
    else:
        return f(n - 1) + n


for r in range(77555533):
    f(r)
print(f(77555533))
# наебал я, короче, рекурсию.....
# у меня заняли вычисления где-то 7 гигов оперативы, так что по-аккуаратнее там

res = '3006975066105829'
print("хош слайсами, хош посчитать, но ласт 7 цифр = 6105829")

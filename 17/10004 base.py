import math


def f(num):
    """Функция для проверки длины числа (чтобы длина == 4)"""
    return 1_000 <= abs(num) < 10_000


nums = [int(r) for r in open('10004 base.txt')]

res = []
real_len_unique_nums = len(nums) // 3

for x, y, z in zip(nums, nums[real_len_unique_nums:], nums[real_len_unique_nums * 2:]):
    s = x + y + z
    if (f(x) + f(y) + f(z) == 2) and (s >= 0) and (math.isqrt(s)) ** 2 == s:
        res.append(s)
print(len(res), min(res))

import math

nums = [int(r) for r in open('17_10004.txt')]

counter_couples = 0
sum_троек = []
for idx in range(len(nums) - 2):
    f, s, t = nums[idx:idx + 3]
    two_of_them_4_разряд = sum([len(str(abs(r))) == 4 for r in nums[idx:idx + 3]]) == 2
    n = f + s + t
    try:
        sum_is_full_квадрат = float(math.sqrt(n)) == int(math.sqrt(n))
    except ValueError:  # если сумма отрицательно. про abs ничего не говорилось, поэтому ставим нуль
        sum_is_full_квадрат = 0
    if two_of_them_4_разряд and sum_is_full_квадрат:
        counter_couples += 1
        sum_троек.append(sum(nums[idx:idx + 3]))
print(counter_couples, min(sum_троек))

# кстати да, можно было обойтись без счетчика, так как counter_couples == len(sum_троек)
print(len(sum_троек))

import itertools


def f(n):
    possible_nums = sorted([int("".join(r)) for r in itertools.permutations(str(n),2) if r[0]!='0'])
    return possible_nums[-1] - possible_nums[0]


c = 0
for r in range(300,401):
    if f(r) == 20:
        c+=1
print(c)
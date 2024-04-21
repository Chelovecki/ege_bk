import itertools


def f(n):
    n = str(n)
    # важно, что именно пары соседних. так что permutations не получиться использовать
    poss_couples = sorted([int(n[r - 1] + n[r]) for r in range(1, len(n))])

    if poss_couples:
        return poss_couples[-1] - poss_couples[0]


print(f"проверка f(2022) = {f(2022)}")

for r in range(10000):
    if f(r) == 44:
        print(r)
        break

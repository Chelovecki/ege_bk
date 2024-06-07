import itertools


def can_have_equal_sum(a, b, c, d):
    alph = a, b, c, d,
    for a, b, c, d in itertools.permutations(alph, 4):
        if a + b == c + d: return True
    return False


numbers = [list(map(int, r.split(';'))) for r in open('4.csv').readlines()]

counter = 0
for line in numbers:
    line.sort()
    if sum(line[:3]) > line[-1]:
        a, b, c, d = line
        if can_have_equal_sum(a, b, c, d):
            counter += 1
print(counter)

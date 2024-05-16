import itertools


def get(line):
    make_str = [str(r) for r in line]
    poss = [list(map(int, r)) for r in itertools.permutations(("17", "21", "16", "59"), 3)]
    return poss


data = [list(map(int, line.split(';'))) for line in open('09 46967.csv').readlines()]
res = []
for line in data:
    flag = False
    poss = get(line)
    for possway in poss:
        first, second, third = possway
        if not (first + second >= third and first + third >= second and second + third >= first):
            flag = True
            break
    if flag:
        res.append(line)

print(len(res))
print(len(data))

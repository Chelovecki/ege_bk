s = open('14647 base.txt').read()

indexes = [idx for idx in range(len(s)) if s[idx] in 'XY']

res = []
for r in range(len(indexes) - 3):
    start = indexes[r + 1]
    end = indexes[r + 3]
    a = s[start:end]
    res.append(len(a))

print(max(res))
s = open('24 59729.txt').read()

idxes = [r for r in range(len(s) - 1) if s[r] + s[r + 1] == 'TT']
m = len(s)
for id in range(len(idxes) - 149):
    obj = idxes[id:id + 150]
    m = min(m, obj[-1] - obj[0] + 2)
print(m)

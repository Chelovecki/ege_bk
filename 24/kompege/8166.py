import itertools

s = open('24_8166.txt').read()
good = ["".join(r) for r in itertools.product('ABC', repeat=2)]

c = m = 0
for repeat in range(2):
    for r in range(repeat, len(s), 2):
        b = s[r - 1] + s[r]
        if b in good:
            c += 1
        else:
            m = max(m, c)
            c = 0
    c = 0

print(m)

# ответ при repeat=0 и repeat=1 один и тот же

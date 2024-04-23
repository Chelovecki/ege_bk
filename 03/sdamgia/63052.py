data = [r.split() for r in open('63052.csv')]

frequensy: dict = dict.fromkeys(set(r[0] for r in data), 0)

for r in data:
    frequensy[r[0]] += int(r[1])

a = list(frequensy.items())
a.sort(key=lambda r: r[1])

print(a[-1])

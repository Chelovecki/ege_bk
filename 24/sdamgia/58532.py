import itertools

print("стыбженное (+ оптимизированное) решение - https://inf-ege.sdamgia.ru/problem?id=58532")
s = open('58532.txt').read()

for r in itertools.permutations("XYZ"):
    s = s.replace("".join(r), "*")
for r in 'XYZ':
    s = s.replace(f"*{r}", "*")

print(max(len(r) for r in s.split('*')))

print("-" * 60)



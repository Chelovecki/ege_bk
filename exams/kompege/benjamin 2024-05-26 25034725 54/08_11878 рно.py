from itertools import product

c_5 = 0
c_6 = 0
for r in product('-.', repeat=5):
    c_5 += 1

for r in product('-.', repeat=6):
    c_6 += 1
print(c_6 + c_5)

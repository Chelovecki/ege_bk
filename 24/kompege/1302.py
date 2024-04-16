s = open('24_1302.txt').read()

# 3 потому что минимально за раз мы должны рассматривать 3 значения (символа)
res = [3] * len(s)

for r in range(3, len(s)):
    if s[r - 3:r + 1] != "XZZY":
        res[r] = res[r - 1] + 1
print(max(res))

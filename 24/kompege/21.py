s = open('24_21.txt').read()

res = [1] * len(s)
for r in range(1, len(s)):
    if s[r] != s[r - 1]:
        res[r] = res[r - 1] + 1
print(max(res))

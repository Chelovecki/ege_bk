s = open('24_4546.txt').read()

aa = ['A' + r + 'A' for r in 'ABC']
cc = ['C' + r + 'C' for r in 'ABC']

res = [0] * len(s)
for r in range(2, len(s)):
    a = s[r - 2:r + 1]
    if a in aa or a in cc:
        res[r] = res[r - 3] + 1
print(max(res))

# --------------------


s = open('24_4546.txt').read()

res = [0] * len(s)
for r in range(2, len(s)):
    a = s[r - 2] + s[r]
    if a == "AA" or a == 'CC':
        res[r] = res[r - 3] + 1
print(max(res))

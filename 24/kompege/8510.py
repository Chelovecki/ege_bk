s = open('24_8510.txt').read()

s = s.replace('O', 'N').replace('P', 'N')

res = [1] * len(s)

for r in range(1, len(s)):
    a = s[r - 1:r + 1]
    if a != 'NN':
        res[r] = res[r - 1] + 1
print(max(res))
# -----------------------------
while 'NN' in s: s = s.replace('NN', 'N N')
print(max(len(r) for r in s.split()))

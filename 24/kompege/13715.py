s = open('24_13715.txt').read()

c = 0
l = 0
m = 0
for r in range(len(s) - 1):
    a = s[r - 1:r + 1]
    if a == 'AB': c += 1
    while c > 50:
        b = s[l:l + 2]
        if b == 'AB': c -= 1
        l += 1
    m = max(m, r - l + 1)
print(m)

s = open('47021.txt').read()

l = c = 0
ca = cb = 0
m=0
for r in range(10, len(s)):
    if s[r] == 'A': ca += 1
    if s[r] == 'B': cb += 1
    if cb > 0 or ca > 2:
        cb = 0
        ca = 0
        l = r
    m = max(m, r - l + 1)
print(m)
#todo
s = open('24_9169.txt').read()

l = 0
c = 0

m = 1_000_000

for r in range(2, len(s)):
    a = s[r - 2:r + 1]
    if a == 'BAD' or a == 'FAT': c += 1

    while c == 3:
        b = s[l:l + 3]
        m = min(m, r - l + 1)
        if b == 'BAD' or b == 'FAT': c -= 1
        l += 1
print(m)

# todo

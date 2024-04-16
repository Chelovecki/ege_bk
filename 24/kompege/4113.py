s = open('24_4113.txt').read()

# s = s.replace('BB', '*').replace('DD', '*')
# for r in 'ABD':
#     s = s.replace(r, ' ')
#
# print(max(len(r) for r in s.split()))


# так как пар ББ ДД может и не быть
res = [0] * len(s)

for r in range(1, len(s)):
    a = s[r - 1] + s[r]
    if a in ('BB', 'DD'):
        # не очень понятно почему именно 2, но я так почувствовал
        res[r] = res[r - 2] + 1
print(max(res))

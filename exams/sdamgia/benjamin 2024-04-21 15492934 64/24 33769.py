import string

s = open('24 33769.txt').read()
print(string.ascii_uppercase)

for r in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    s = s.replace(r + r, ' ')

res: dict = dict.fromkeys('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 0)

for seq in s.split():
    first_letter = seq[0]
    res[first_letter] += 1


print(max(res.values()))

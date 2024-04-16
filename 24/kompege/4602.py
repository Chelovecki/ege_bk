s = open('24_4602.txt').read()

for r in 'DC':
    s = s.replace(r, 'B')
s = s.replace('O', 'A')

s = s.replace('BA', '*').replace('B', ' ').replace('A', ' ')

print(max(len(r) for r in s.split()))

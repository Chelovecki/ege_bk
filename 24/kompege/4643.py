s = open('24_4643.txt').read()

s = s.replace('2', '1').replace('B', 'A')
s = s.replace('11A', '*')

for r in 'A1':
    s = s.replace(r, ' ')

print(max(len(r) for r in s.split()))

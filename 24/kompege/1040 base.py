s = open('24_1040.txt').read()

for r in 'QWERTYUIOPASDFGHJKLZXCVBNM'.lower():
    s = s.replace(r, ' ')

for r in '012345678':
    s = s.replace(r, '9')
print(max(len(r) for r in s.split()))

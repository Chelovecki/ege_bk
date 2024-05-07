s = open('24_11241.txt').read()

for r in 'ABCD':
    s = s.replace(r, ' ')

print(max(len(r) for r in s.split()))

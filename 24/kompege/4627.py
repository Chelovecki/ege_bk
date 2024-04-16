s = open('24_4627.txt').read()

s = s.replace('NPO', '*').replace('PNO', '*')
for r in 'NPO':
    s = s.replace(r, ' ')

print(max(len(r) for r in s.split()))

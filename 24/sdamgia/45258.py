s = open('45258.txt').read()

s = s.replace('AB', '*').replace('CB', '*')

for r in 'ABC':
    s = s.replace(r, ' ')

print(max([len(r) for r in s.split()]))


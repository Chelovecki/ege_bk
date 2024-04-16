s = open('2426.txt').read()

for r in "ABC":
    s = s.replace(r, " ")

for r in '12':
    s = s.replace(r,'3')

print(max(len(r) for r in s.split()))
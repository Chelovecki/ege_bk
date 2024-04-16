s = open('24_1428.txt').read()

s = s.replace('XY', 'X Y').replace('XZ', 'X Z')

print(max(len(r) for r in s.split()))

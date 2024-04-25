s = open('27697.txt').read()
print(max([len(r) for r in s.replace('L', ' ').replace('R', ' ').split()]))

print('-'*30)

s = open('27697.txt').read()

print('D'*12 in s)
print('D'*11 in s)
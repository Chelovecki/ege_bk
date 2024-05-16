s = open('24 68525.txt').read()

s = s.replace('R', 'Q').replace('W', 'Q').replace('2', '1').replace('4', '1')

s = s.replace('QQ', 'Q Q').replace('11', '1 1')

print(max([len(r) for r in s.split()]))

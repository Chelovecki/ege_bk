s = open('29672.txt')

c = 0
for line in s.readlines():
    if line.count('E') > line.count('A'): c += 1
print(c)


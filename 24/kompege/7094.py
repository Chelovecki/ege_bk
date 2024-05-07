s = open('24_7094.txt').read()

s = s.replace('U', 'A').replace('D', 'C').replace('F', 'C')

print('CA' * 173 in s)
print(len(('CA' * 173)) // 2)


# //2 потому что нужно кол-во пар

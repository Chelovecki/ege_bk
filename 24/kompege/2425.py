s = open('24_2425.txt').read()

print('DBAC'*23 in s)
print('DBAC'*23 + 'D' in s)
print('DBAC'*23 + 'DB' in s)
print('DBAC'*23 + 'DBA' in s)
print('DBAC'*23 + 'DBA' in s)
print('DBAC'*23 + 'DBAC' in s)
print(len('DBAC'*23 + 'DBA'))
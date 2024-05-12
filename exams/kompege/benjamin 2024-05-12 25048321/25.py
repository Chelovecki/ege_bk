from fnmatch import fnmatch

c = 0
for r in range(8, 680_000, 8):
    if fnmatch(str(r), '1*2*2'): c += 1
print(c)

from fnmatch import fnmatch

for r in range(0, 10 ** 10, 1917):
    if fnmatch(str(r), '3?12?14*5'):
        print(r, r // 1917)

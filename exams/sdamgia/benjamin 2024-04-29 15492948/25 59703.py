from fnmatch import *

for r in range(0, 10 ** 8, 2023):
    if fnmatch(str(r), '3?1*57'):
        print(r, r // 2023)

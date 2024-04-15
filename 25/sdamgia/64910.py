from fnmatch import *

for r in range(0, 10 ** 10, 1987):
    if fnmatch(str(r), '1*4022?9'):
        print(r)

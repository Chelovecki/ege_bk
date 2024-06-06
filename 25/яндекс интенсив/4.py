from fnmatch import *

for r in range(7977,10**9, 7977):
    if fnmatch(str(r), '?1*23*92'):
        print(r, r//7977)
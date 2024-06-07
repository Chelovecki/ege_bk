from fnmatch import *

for r in range(13, 10**8, 13):
    if fnmatch(str(r), '123*678'):
        print(r, r//13)
from fnmatch import *

for r in range(10 ** 10):
    if r % 4173 == 0 and fnmatch(str(r), '1?2655*8'):
        print(r)

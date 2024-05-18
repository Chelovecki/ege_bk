import math
from fnmatch import fnmatch

for r in range(2024, 10 ** 10, 2024):
    if fnmatch(str(r), '1?2*4'):
        if int((r ** 0.5)) == math.sqrt(r):
            print(r, r // 2024)

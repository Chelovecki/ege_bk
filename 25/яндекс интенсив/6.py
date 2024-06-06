from fnmatch import *

for r in range(42, 2*10**8, 42):
    if not fnmatch(str(r), '1*7*') and fnmatch(str(r), '?2*4*0'):
        print(r,r//42)
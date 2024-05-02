from itertools import *

for n, r in enumerate(product('АОУ', repeat=5), 1):
    if n==210:
        print("".join(r))

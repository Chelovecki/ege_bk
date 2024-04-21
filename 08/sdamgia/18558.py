from itertools import *

c = 0
for r in product("иван", repeat=5):
    if r.count("и") >= 1:
        c += 1
print(c)

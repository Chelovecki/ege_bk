from fnmatch import *

for r in range(1991, 10 ** 10, 1991):
    if fnmatch(str(r), '1*4182?7'):
        print(r)
# еблантяй, ждал пока ренж от 10**10 выдаст ответ)))
# а потом я вспомнил про шаг...

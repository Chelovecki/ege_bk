from ipaddress import *

c = 0
for n in ip_network('123.222.111.192/255.255.255.248', 0):
    n = [bin(int(r))[2:].zfill(8) for r in str(n).split('.')]
    if n[3].count('1') % 3 != 0: c += 1
print(c)

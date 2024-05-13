from ipaddress import *

c = 0
for n in ip_network('192.168.32.48/255.255.255.240'):
    n = "".join([bin(int(r))[2:] for r in str(n).split('.')]).count('1')
    if n % 2 != 0: c += 1
print(c)

from ipaddress import *

c=0
for n in ip_network('195.102.65.64/255.255.255.192',0):
    n = [bin(int(r))[2:].zfill(8) for r in str(n).split('.')]
    if n[-1].count('0') == n[-1].count('1'):
        c+=1
print(c)
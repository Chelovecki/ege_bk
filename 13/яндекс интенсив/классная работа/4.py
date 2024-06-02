from ipaddress import *

c = 0
for a in range(200):
    flag = True
    for n in ip_network(f'183.192.{a}.0/255.255.252.0', 0):
        n = [bin(int(r))[2:].zfill(8) for r in str(n).split('.')]
        right_2 = (n[2] + n[3]).count('1') > 3
        if not right_2:
            flag = False
            break
    if flag:
        print(a)
        break

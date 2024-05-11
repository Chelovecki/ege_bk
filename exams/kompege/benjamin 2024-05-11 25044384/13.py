from ipaddress import *


def check(ipadr):
    ipadr = str(ipadr)
    ipadr = [bin(int(r))[2:].zfill(8) for r in ipadr.split('.')]
    return ipadr[0].count('1') + ipadr[1].count('1') >= ipadr[2].count('0') + ipadr[3].count('0')


for a in range(256):
    net = ip_network(f"238.51.1.202/255.255.{a}.0", 0)
    for r in net:
        print(r)
    # if all(check(n) for n in net):
    #     print(a)
    #     break

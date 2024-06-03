from ipaddress import *

for mask in range(18, 30):
    net = ip_network(f'215.181.200.27/{mask}', 0)
    for n in net:
        if str(n) == '215.181.192.0':
            print(net.netmask)
print("-" * 30)

print(bin(200)[2:].zfill(8))
print(bin(192)[2:].zfill(8))
print(int('11110000', 2))
print("-" * 30)

print("итого, макс значение - 240")

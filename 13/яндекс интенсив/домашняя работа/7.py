from ipaddress import *

ip = ip_address('76.155.48.0')
res = set()
for mask in range(17, 31):
    net = ip_network(f'76.155.48.2/{mask}', 0)
    for n in net:
        if n == ip:
            print(net, )
            # res.add(mask)
            res.add(net.netmask)
print("итого,", len(res))
print("посчиталось как 14, но видно, что с 17 по 19 3-й слева бит != 48. так что получаем 30-19=11 значений")

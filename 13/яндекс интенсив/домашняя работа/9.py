from ipaddress import *

res = set()
for m in range(14,31):
    net = ip_network(f'158.116.11.146/{m}', 0)
    for n in net:
        if str(n) == "158.116.0.0":
            print(net)
            # res.add(m)
            res.add(net.netmask)
print("правильные ip (3-й байт == 116) начинаются с значения 14 в ренже,поэтому ответ:", len(res))


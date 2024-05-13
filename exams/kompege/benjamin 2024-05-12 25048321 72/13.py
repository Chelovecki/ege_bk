from ipaddress import *

c = 0
net = ip_network('192.168.32.128/255.255.255.192', 0)

for n in net:
    n = str(n)
    # в двоичное представление
    n = [bin(int(obj))[2:] for obj in n.split('.')]
    # считаем едининицы
    n = [obj.count('1') for obj in n]

    if sum(n) % 2 == 1:
        c += 1
print(c)

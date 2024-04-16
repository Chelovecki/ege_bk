"""
№ 12451 (Уровень: Средний)

(Д. Иванов) В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и маске сети.

Сеть, в которой содержится узел с IP-адресом 246.81.65.A, задана маской сети 255.255.255.224, где A - некоторое допустимое для записи IP-адреса число. Определите количество значений A, для которых у всех узлов в этой сети в двоичной записи количество нулей в третьем байте больше, чем в четвертом.
"""
import ipaddress

res = []
for a in range(256):
    f = True
    ip = f'246.81.65.{a}'
    net = ipaddress.ip_network(f'{ip}/255.255.255.224', 0)
    if ip not in (str(net.network_address), str(net.broadcast_address)):
        for node in net.hosts():
            bet = [bin(r)[2:] for r in map(int, str(node).split('.'))]
            tri = bet[2]
            chetire = bet[3]
            if tri.count('0') <= chetire.count('0'):
                f = False
                break
        if f:
            res.append(a)

print(len(res))

# str(net.) потому что нужно сравнивать строки с ip.
# ip - это str. так что адрес сети и широковещательный мы тоже приведем к виду str


# а вообще, тут чел хорошо объясняют как сети работают https://youtu.be/drJkbXoNxyI?t=2603
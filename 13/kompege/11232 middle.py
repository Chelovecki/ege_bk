"""
№ 11232 (Уровень: Средний)

(М. Ишимов) В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и маске сети.
Сеть задана IP-адресом 192.168.31.80 и маской сети 255.255.255.240. Определите максимальную сумму единиц в двоичной записи IP-адреса в этой сети.

В ответе укажите только число.
"""

import ipaddress

res = set()
for ip in ipaddress.ip_network(f'192.168.31.80/255.255.255.240', 0):
    res.add(f'{ip:b}'.count('1'))
print(max(res))
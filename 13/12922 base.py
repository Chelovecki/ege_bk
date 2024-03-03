"""
№ 12922 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)

В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и маске сети.

Сеть задана IP-адресом 136.36.240.16 и маской сети 255.255.255.248.

Сколько в этой сети IP-адресов, в которых в двоичной записи IP-адреса не встречается 101?

В ответе укажите только число.
"""

import ipaddress

c = 0
for net in ipaddress.ip_network('136.36.240.16/255.255.255.248'):
    bin_net = "".join([bin(int(part))[2:] for part in str(net).split('.')])
    if '101' not in bin_net:
        c += 1
print(c)
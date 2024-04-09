"""
№ 14648 Открытый курс "Слово пацана" (Уровень: Базовый)

(М. Попков) В терминологии сетей TCP/IP маска сети – это двоичное число, меньшее 232; в маске сначала (в старших разрядах) стоят единицы, а затем с некоторого места нули. Маска определяет, какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу самого узла в этой сети. Обычно маска записывается по тем же правилам, что и IP-адрес – в виде четырёх байт, причём каждый байт записывается в виде десятичного числа. Адрес сети получается в результате применения поразрядной конъюнкции к заданному IP-адресу узла и маске.

Для узла c IP-адресом 218.48.192.56 адрес сети равен 218.48.192.0. Сколько существует различных возможных значений третьего слева байта маски, если известно, что в этой сети не менее 500 узлов? Ответ запишите в виде десятичного числа.
"""

import ipaddress

res = []
for net in ipaddress.ip_network('203.111.195.0/255.255.240.0', 0):
    bet = f"{net:b}"
    if bet.count('0') % 3 == 0 and '000' in bet and '111' in bet:
        res.append(bet)
print(len(res))

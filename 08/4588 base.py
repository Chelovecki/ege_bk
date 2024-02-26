"""
№ 4588 Основная волна 2022 (Уровень: Базовый)

Определите количество пятизначных чисел, записанных в восьмеричной системе счисления, в записи которых ровно одна цифра 6, при этом никакая нечётная цифра не стоит рядом с цифрой 6.
"""

from itertools import product

c = 0
for r in product('01234567', repeat=5):
    if r[0] != '0':
        if r.count('6') == 1:
            idx_of_6 = r.index('6')
            # крайний справа элемент (последний)
            if idx_of_6 == 4:
                first = int(r[idx_of_6 - 1])
                second = 0
            # крайний слева элемент (первый)
            elif (idx_of_6 == 0):
                first = 0
                second = int(r[idx_of_6 + 1])
            else:
                numbers = r[idx_of_6 - 1: idx_of_6 + 2]
                first = int(numbers[0])
                second = int(numbers[2])
            if first % 2 != 1 and second % 2 != 1:
                c += 1
print(c)

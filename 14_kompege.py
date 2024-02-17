# № 11317 (Уровень: Базовый)
#
# (М. Ишимов) Операнды арифметического выражения записаны в системе счисления с основанием 17.
#
# 7ACx53D17+83BG94xD17+C5xD17+C4BBFx417+7x79177ACx53D17​+83BG94xD17​+C5xD17​+C4BBFx417​+7x7917​
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита 17-ричной системы счисления. Определите наибольшее значение x, при котором значение данного арифметического выражения кратно 16. Для найденного x вычислите частное от деления значения арифметического выражения на 16 и укажите его в ответе в десятичной системе счисления. Основание системы счисления указывать не нужно.
# -------------------------------------------

# for x in range(17): работать не будет, а вот
# for x in '0123456789abcdefg': будет работать 🤔
for x in '0123456789abcdefg':
    #  сделал так странно списком, чтобы удобнее было смотреть и заполнять слагаемые
    number = sum([
        int(f'7ac{x}53d', 17),
        int(f'83bg94{x}d', 17),
        int(f'c5{x}d',17),
        int(f'c4bbf{x}4',17),
        int(f'7{x}79', 17)
    ])

    if number % 16 == 0:
        print(number//16)


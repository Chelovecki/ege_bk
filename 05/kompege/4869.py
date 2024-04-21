def f(n: int):
    bin_n = bin(n)[2:]
    # убираем ведущие нули
    while bin_n and bin_n[0] == '0': bin_n = bin_n[1:]

    # считаем нужные нули единицы.
    # жеский обсёр может произойти, если не обратить внимание на формулировку
    # "(от старших разрядов к младшим, начиная с единицы).", то есть, надо считать чет/нечет с единицы, а не с 0
    odin_on_chet = len([bin_n[idx] for idx in range(len(bin_n)) if (idx + 1) % 2 == 0 and bin_n[idx] == '1'])
    zero_on_nechet = len([bin_n[idx] for idx in range(len(bin_n)) if (idx + 1) % 2 != 0 and bin_n[idx] == '0'])

    return abs(odin_on_chet - zero_on_nechet)


print(f"проверка: f(39) = {f(39)}")

for r in range(2, 10000):
    if f(r) == 5:
        print(r)
        break

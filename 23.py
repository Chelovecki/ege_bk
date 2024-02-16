# № 8685 (Уровень: Средний)
#
# (М. Шагитов)  Исполнитель преобразует число, записанное на экране. У исполнителя есть три команды, каждой из которых присвоен номер:
#
#     Прибавить 3
#     Прибавить 5
#     Умножить на 2
#
# Первая команда увеличивает число на 3, вторая – на 5, третья удваивает число. Программа для исполнителя – это последовательность команд.
#
# Укажите количество программ, которые преобразуют исходное число 4 в число 68. При этом траектория вычислений программы должна проходить через число 16 или 32, но не через оба эти числа одновременно.
# ----------------------------------------------------------------

def f(current, end, flag: str):
    if current > end or ('16' in flag and '32' in flag):
        return 0
    if current == end and ('16' in flag or '32' in flag):
        return 1

    res = [
        f(current + 3, end, flag + f" {str(current)}"),
        f(current + 5, end, flag + f" {str(current)}"),
        f(current * 2, end, flag + f" {str(current)}"),
    ]

    return sum(res)


print(f(4,68,''))

# если запустить без and ('16' in flag or '32' in flag), то будет не тот результат 🤔
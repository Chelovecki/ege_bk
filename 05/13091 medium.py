"""
№ 13091 (Уровень: Средний)
Алгоритм получает на вход натуральное число N и строит по нему новое число R следующим образом.
1) Строится двоичная запись числа N.
2) В конец двоичной записи добавляется двоичный код остатка от деления числа N на 4
3) Результатом работы алгоритма становится десятичная запись полученного числа R.
Пример 1 Дано число N = 13 Алгоритм работает следующим образом.
1) Строим двоичную запись: 1310 = 11012
2) Остаток от деления 13 на 4 равен 1, добавляем к двоичной записи цифру 1, получаем 110112 = 2710
3) Результат работы алгоритма R = 27
Пример 2 Дано число N = 14 Алгоритм работает следующим образом.
1) Строим двоичную запись: 1410 = 11102
2) Остаток от деления 14 на 4 равен 2, добавляем к двоичной записи цифры 10 (102 = 210), получаем 1110102 = 5810
3) Результат работы алгоритма R = 58
Назовем доступными числа, которые могут получиться в результате работы этого алгоритма. Например, числа 27 и 58 – доступные.
Какое наибольшее количество доступных чисел может быть на отрезке, содержащем 65 натуральных чисел?
"""


def funk(n: int):
    # num = bin(n)[2:]
    num = f'{n:b}'
    # можно использовать оба варианта. я только что узнал про используемый.
    num += f'{(n % 4):b}'
    return int(num, 2)


print(f"проверка. 13 = {funk(13)}; 14 = {funk(14)}")

# генерируем список с результатами работы функции
res = []
for r in range(10_000):
    res.append(funk(r))

# Создаем список. мы будем обращаться к индексу по значениям res
#     Поясняю: в new_list 100к значений (взяли с запасом). Проходя по списку res, мы будем получать разные значения (работы функции).
#     Эти значения мы будем использовать в качестве индекса в new_list. Значение в этой ячейке = 1.
#     Таким образом можно будет находить сумму
new_list = [0] * 100_000

for r in res:
    new_list[r] = 1

# И здесь мы берем куски по 65 значений, и смотрим максимальную сумму.
print("ответ:", max(sum(new_list[idx:idx + 65]) for idx in range(len(new_list) - 65)))
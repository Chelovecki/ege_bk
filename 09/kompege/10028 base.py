"""
№ 10028 (Уровень: Базовый)

(С. Чайкин) Откройте файл электронной таблицы, содержащей в каждой строке четыре натуральных числа. Определите сумму номеров строк таблицы, для чисел которой выполнено только одно условие:
– в строке есть повторяющиеся числа;
– произведение минимальное и максимального чисел не превышает суммы оставшихся;
 – четыре числа можно разбить на два пары чисел с равными суммами.

В ответе запишите только число.
"""
numbers = [list(map(int, row.split(','))) for row in open('10028 base.csv')]
sum_num_rows = 0
for n, row in enumerate(numbers, 1):
    bool_nums_repeat = len(row) > len(set(row))

    row = sorted(row)
    bool_proizv_max_min_more = min(row) * max(row) <= row[1] + row[2]

    first, second, third, forth = row
    couples = [
        # 1+4==2+3
        first + forth == second + third,
        # 1+2==3+4
        first + second == third + forth,
        # 1+3==2+4
        first + third == second + forth
    ]
    bool_couples = sum(couples) >= 1

    if (bool_couples + bool_nums_repeat + bool_proizv_max_min_more) == 1:
        sum_num_rows += n
print(sum_num_rows)
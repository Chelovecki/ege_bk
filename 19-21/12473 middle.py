"""
№ 12473 PRO100 ЕГЭ 29.12.23 (Уровень: Средний)

Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча снежков. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в кучу один снежок или увеличить количество снежков в куче в два раза. Для того чтобы лепить снежки, у каждого игрока есть неограниченное количество снега.

Игра завершается в тот момент, когда количество снежков в куче становится не менее 129. Проигравшим считается игрок, сделавший последний ход, т.е. первым получивший кучу из 129 или более снежков.

В начальный момент в куче было S снежков, 1 ≤ S ≤ 128.

Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.

Укажите минимальное значение S, при котором при любой игре Пети Ваня может выиграть, сделав не более одного хода.
"""

"""
Задание 20.

Для игры, описанной в задании 19, найдите два наименьших значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:

    – Петя не может выиграть, сделав один ход;
    – Петя может выиграть, сделав не более двух ходов независимо от того, как будет ходить Ваня.

Найденные значения запишите в ответе в порядке возрастания.
"""

"""
Задание 21.

Для игры, описанной в задании 19, найдите количество значений S, при которых одновременно выполняются два условия:

    – у Вани есть выигрышная стратегия, позволяющая ему выиграть, сделав не более двух ходов при любой игре Пети;
    – у Вани нет стратегии, которая позволит ему гарантированно выиграть, сделав не более одного хода.
"""


def f(a, m):
    if a >= 129: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a + 1, m - 1),
        f(a * 2, m - 1)
    ]
    return any(h) if m % 2 != 0 else all(h)


print("19)", [r for r in range(1, 129) if not f(r,2) and f(r,1)])

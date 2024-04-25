"""
№ 12928 PRO100 ЕГЭ 26.01.24 (Уровень: Средний)

Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в кучу один камень или увеличить количество камней в куче в два раза. Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней.

Игра завершается в тот момент, когда количество камней в куче становится не менее 21. Победителем считается игрок, сделавший последний ход, т.е. первым получивший кучу из 21 или больше камней.

В начальный момент в куче было S камней, 1 ≤ S ≤ 20.

Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.

Найдите минимальное значение S, при котором у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:

    – Петя не может выиграть за один ход;
    – Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.

Задание 20.

Для игры, описанной в задании 19, найдите минимальное значение S, при котором одновременно выполняются два условия:

    – у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
    – у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.

Задание 21.

Для игры, описанной в задании 19, найдите два минимальных значения S, при которых одновременно выполняются три условия:

    – у Пети есть выигрышная стратегия, позволяющая ему выиграть первым, вторым или третьим ходом при любой игре Вани;
    – у Пети нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
    – у Пети нет стратегии, которая позволит ему гарантированно выиграть первым или вторым ходом.

Найденные значения запишите в ответе в порядке возрастания.
"""


def f(s, m):
    if s >= 21: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m - 1), f(s * 2, m - 1)]

    return any(h) if m % 2 != 0 else all(h)


print("19)", min([s for s in range(1, 21) if not f(s, 1) and f(s, 3)]))
print("20)", min([s for s in range(1, 21) if f(s, 2) or f(s, 4) and not f(s, 2)]))
print("21)", [s for s in range(1, 21) if not f(s, 1) and not f(s, 3) and f(s, 5)])
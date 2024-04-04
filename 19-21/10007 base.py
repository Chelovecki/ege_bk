"""
№ 10007 (Уровень: Базовый)

(С. Чайкин) Два игрока, Полина и Вика, играют в следующую игру. Перед игроками лежат две кучи камней. Игроки ходя по очереди, первый ход делает Полина. За один ход игрок может добавить в одну из куч (по своему выбору) один или пять камней или увеличить их количество в два раза. Игроки не могут изменять количество камней в одной куче больше двух раз подряд. Игра завершается в тот момент, когда произведение камней в кучах будет не менее 512. Победителем считается игрок, сделавший последний ход.

Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника. Какое наименьшее число камней могло быть суммарно в двух кучах если известно, что Вика выигрывает первым ходом при любой игре Полины.
"""

"""
Задание 20.

В игре, описанной в задании 19, в начальный момент в первой куче было 5 камней, во второй – S камней, 1 ≤ S ≤ 102

Найдите наименьшее значения S, при которых Полина не может выиграть первым ходом, но у неё есть выигрышная стратегия, позволяющих ей выиграть вторым ходом при любой игре Вики.
"""

"""
Задание 21.

В игре, описанной в задании 19, в начальный момент в первой куче было 10 камней, во второй – S камней, 1 ≤ S ≤ 51

Найдите два наибольших значения S, при которых Вика не может выиграть первым ходом, но у неё есть выигрышная стратегия, позволяющих ей выиграть вторым ходом при любой игре Полины. Найденные значения запишите в ответе в порядке убывания.
"""


def f(s1, s2, step, p1=0, p2=0):
    """
    Функция, которая рекурсивно обрабатывает все возможные комбинации ходов
    :param s1: кол-во камней в 1 куче
    :param s2: кол-во камней в 2 куче
    :param step: кол-во ходов (хз)
    :param p1: сколько раз игрок 1 использовал одну и ту же комбинацию (должно быть не более 2х раз по условию)
    :param p2: сколько раз игрок 2 использовал одну и ту же комбинацию (должно быть не более 2х раз по условию)
    :return: список из возможных ходов при определенных s1, s2 и step
    """
    if s1 * s2 >= 512: return step % 2 == 0
    if step == 0: return 0
    ways = []
    if p1 < 2:
        ways += [
            f(s1 + 1, s2, step - 1, p1 + 1, 0),
            f(s1 + 5, s2, step - 1, p1 + 1, 0),
            f(s1 * 2, s2, step - 1, p1 + 1, 0)
        ]
    if p2 < 2:
        ways += [
            f(s1, s2 + 1, step - 1, 0, p2 + 1),
            f(s1, s2 + 5, step - 1, 0, p2 + 1),
            f(s1, s2 * 2, step - 1, 0, p2 + 1)
        ]
    return any(ways) if step % 2 else all(ways)


def num_19():
    print("19)", min([s1 + s2
                      for s1 in range(1, 512)
                      for s2 in range(1, 512)
                      if f(s1, s2, 2)
                      ]
                     )
          )


def num_20():
    print("20)", min([r for r in range(1, 103) if not f(5, r, 1) and f(5, r, 3)]))


def num_21():
    print("21)", [r for r in range(1, 52) if not f(10, r, 2) and f(10, r, 4)][::-1])


num_19()
num_20()
num_21()

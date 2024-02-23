"""
№ 11841 (Уровень: Базовый)

(Л. Шастин) Исполнитель преобразует число на экране. У исполнителя есть три команды, которые обозначены латинскими буквами:

А. Вычесть 2
В. Вычесть 3
С. Найти целую часть от деления на 5

Программа для исполнителя — это последовательность команд.
Сколько существует программ, для которых при исходном числе 41 результатом является число 5, при этом траектория вычислений не содержит числа 20 и содержит 10?
Траектория вычислений программы — это последовательность результатов выполнения всех команд программы.
Например, для программы СВА при исходном числе 51 траектория будет состоять из чисел 10, 7, 5.
"""

def f(a,b):
    if a<b or a==20:return 0
    if a==b:return 1

    return f(a-2,b)+f(a-3,b)+f(a//5,b)

print(f(41,10) *f(10,5))
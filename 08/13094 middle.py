"""
№ 13094 (Уровень: Средний)
Сколько существует 9-значных девятеричных чисел, в записи которых не встречается цифра 0, любые две соседние цифры имеют разную чётность, и никакая цифра не повторяется больше 3 раз?
"""
from itertools import product

# кабанов гениально решил избавиться от 2-го условия прям на уровне подачи данных
chet_nums = '2468'
nechet_nums = '1357'

counter = 0
for r in product(chet_nums, nechet_nums, chet_nums, nechet_nums, chet_nums,nechet_nums,chet_nums,nechet_nums,chet_nums):
    r = ''.join(r)
    # в списке данные вида
    # [False, False, False, False, False, False, False, False, False]
    if all([r.count(x) <=3 for x in r]):
        counter += 1
print(counter)


"""
Комментарии по решению

Так как в оригинале у нас 9**9 вариантов, что дофига, поэтому надо оптимизировать.

Мы рассмотрим 2 варианта, когда последовательность 
1) "чет-нечет-...-чет", и когда 
2) "нечет-чет-...-нечет"

Поэтому в цикле мы пишем такую херовину: chet_nums, nechet_nums, chet_nums, nechet_nums, chet_nums,nechet_nums,chet_nums,nechet_nums,chet_nums
В результате мы получаем такой ответ: 241920
Результат в product зависит от кол-ва чисел (при неизменном алфавите), поэтому значение для 1 и 2 варианта равны, значит надо ответ умножить на 2.

Ну или можно ручками поменять чет на нечет; нечет на чет и самому проверить
"""
"""
№ 10006 (Уровень: Базовый)

(С. Чайкин) Все восьмибуквенные слова, составленные из букв русского алфавита, записаны в алфавитном порядке и пронумерованы.

Ниже приведено начало списка.
1. АААААААА
2. АААААААБ
3. АААААААВ
4. АААААААГ
5. АААААААД

Под каким номером стоит слово РЕКУРСИЯ?

Показать ответ
731425709058
"""
def cc(word, data: dict, base):
    word = word[::-1]
    also_res = [data[word[idx]] * len(data) ** idx for idx in range(len(word))]
    return sum(also_res) + 1
    # word = word[::-1]
    # res = 0
    # for idx in range(len(word)):
    #     a = n_by_row[word[idx]]
    #     b = len(n_by_row)
    #     c = idx
    #     r = a*b**c
    #     res += r
    # return res + 1


rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

data = {rus_alph[idx]: idx + 1 for idx in range(len(rus_alph))}

print(cc('рекурсия', data, rus_alph))

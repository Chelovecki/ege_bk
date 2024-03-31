import time
from itertools import product
# получаем рус алфавит. в него надо будет вручную дописать ё
start_a = ord('а') # русская а
print("".join(chr(r) for r in range(start_a, start_a+32)))

alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
a = time.time()
for n, r in enumerate(product(alph, repeat=8), 1):
    print(r)
    if r[0] == "р" and r[1] == "е" and r[2] == "к" and r[3] == "у" and r[4] == "р" and r[5] == "с" and r[6] == "и" and r[7] == "я":
        print(n)
        print(f"выполнено за {time.time() - a} сек.")
        break
from itertools import product

for n, r in enumerate(product(sorted('компьютер'), repeat=5),1):
    r = "".join(r)
    if r.count('к') == 2 and r[0]!= 'ь' and n%2 ==1:
        print(n,r)
print("ответ - ласт номер")
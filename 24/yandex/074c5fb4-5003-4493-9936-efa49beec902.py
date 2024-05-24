# https://education.yandex.ru/ege/task/074c5fb4-5003-4493-9936-efa49beec902

s = open('074c5fb4-5003-4493-9936-efa49beec902.txt').read()

a = ["Dasher", "Dancer", "Blitzen", "Donner", "Cupid", "Comet", "Vixen", "Prancer"]

for r in a:
    s = s.replace(r, " " + r + " ")

b = dict.fromkeys(a, 0)

for r in s.split():
    b[r] += 1
print(b)

print("макс значение у кометы = 37")

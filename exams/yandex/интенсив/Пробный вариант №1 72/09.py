import string

numbers = [list(map(int, r.split(';'))) for r in open('9.csv').readlines()]
c = 0
for line in numbers:
    if line == sorted(line) and len(line) == len(set(line)):
        c += 1
print(c)
print(f'латиница: 150 bit')
print(f'пол: 2 bit')
print(f'дата рождения: 32 bit')
"""
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом.

Например, в тексте ABCAABAKLD самая длинная цепочка символов, удовлетворяющая условию  — ABCAABAK, её длина равна 8.

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
"""

s = open('37131.txt').read()

while 'KL' in s: s = s.replace('KL', "K L").replace("LK", "L K")

print(max(len(r) for r in s.split()))

# стоит учесть как KL, так и LK.... хм

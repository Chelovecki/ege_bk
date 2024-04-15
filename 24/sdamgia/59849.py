"""
Текстовый файл состоит не более чем из 106 символов латинского алфавита. Необходимо найти самую длинную подстроку, содержащую символы из алфавита 26 системы счисления. В ответ записать длину последовательности символов, которая может являться числом в 26 системе счисления.
"""
import string

s = open('59849.txt').read()
# print(string.ascii_letters)
alphabet_of_26_cc = "0123456789ABCDEFGHIJKLMNOP"

for r in set(s):
    if r not in alphabet_of_26_cc:
        s = s.replace(r, " ")

print(max(len(r) for r in s.split()))

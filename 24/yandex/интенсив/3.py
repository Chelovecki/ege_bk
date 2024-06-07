import string

s = open('3.txt').read()

for letter in string.ascii_uppercase:
    s = s.replace(letter, ' ')

print(max(int(r) for r in s.split()))
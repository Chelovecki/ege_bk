# https://education.yandex.ru/ege/task/a63bca73-d464-4237-a1f3-60131bbbee77
import string

s = open('a63bca73-d464-4237-a1f3-60131bbbee77.txt').read()

# s= '0XY3Z9ABC1948FRG2333W4'

for symb in string.ascii_uppercase:
    s=s.replace(symb, 'A')

m = len(s)
c=1
boba = '0123456789ABCDEF'
temp = ''
for idx in range(1,len(s)):
    a = s[idx-1]
    b = s[idx]
    if a <= b:
        temp += a
    else:
        m=min(m,len(temp))
        temp=''
    # print(a,b)
print(m)
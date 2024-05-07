import string

s = open('24_14646.txt').read()

freq = dict.fromkeys(string.ascii_uppercase, 0)

c = m = 0
flag = False
for idx in range(2, len(s)):

    a = s[idx - 2:idx + 1]

    if flag:
        freq[s[idx]] += 1
        flag = False
    if len(set(a)) == 1:
        flag = True

print(sorted(freq.items(), key=lambda x: x[1])[-1])

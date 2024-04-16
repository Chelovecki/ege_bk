s = open('24_2423.txt').read()

res = [1]*len(s)

for r in range(1, len(s)):
    if s[r-1] < s[r]:
        res[r] = res[r-1]+1
print(max(res))
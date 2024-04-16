s = open('24_9552.txt').read()

res = [0]*len(s)

for r in range(1, len(s)):
    pc = s[r-1] + s[r]
    if pc == "PC":
        res[r] = res[r-2]+2

    if r >= 3:
        csgo = s[r-3:r+1]
        if csgo == "CSGO":
            res[r] = res[r-4]+4
print(max(res))
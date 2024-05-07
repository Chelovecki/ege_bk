f = open('24_14100.txt')
s = f.readline()
dp = [0] * len(s)
good_seq = ['ABA', 'CB', 'AC', 'BB', 'ABC', 'BCB', 'BA', 'AB']
с = m = 0
for idx in range(1, len(s)):
    for obj in good_seq:
        if idx >= len(obj) - 1:
            if s[idx - len(obj) + 1:idx + 1] == obj:
                # idx - len(obj) - это индекса, с которого начинается этот obj (или длится)
                dp[idx] = max(dp[idx], dp[idx - len(obj)] + len(obj))
print(max(dp))

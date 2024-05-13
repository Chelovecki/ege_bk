nums = [int(r) for r in open('17.txt').readlines()]
max_krat_221 = max([r for r in nums if str(r).endswith('221')])

c = 0
m = 100_000 * 3
for r in range(2, len(nums)):
    a = nums[r - 2:r + 1]

    odnoznach = [n for n in a if abs(n) > 9 and int(str(n)[-2]) % 2 != 0]
    if len(odnoznach) == 2:
        if len([n for n in a if len(str(abs(n))) == 2]) <= 2:
            if sum(a) > max_krat_221:
                c += 1
                m = min(sum(a), m)
print(c, m)

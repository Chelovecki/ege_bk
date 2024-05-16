nums = [int(r) for r in open('26 68527.txt').readlines()]

total = nums[0]
nums = sorted(nums,reverse=True)

res = []


for start_idx in range(len(nums)):
    temp = [nums[start_idx]]
    for end_idx in range(start_idx+1, len(nums)):
        num = nums[end_idx]
        if abs(temp[-1] - num) >= 4:
            temp.append(num)
    res.append(temp)

res.sort(key=lambda x:len(x))

print(len(res[-1]), min(res[-1]))

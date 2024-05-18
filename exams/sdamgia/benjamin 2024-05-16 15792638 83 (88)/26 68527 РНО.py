nums = [int(r) for r in open('26 68527.txt').readlines()]

init_diametr = nums[0]
nums = sorted(nums, reverse=True)

res = []

c = 0
for start_idx in range(1, len(nums)):
    curr_diametr = nums[start_idx]
    if init_diametr - curr_diametr >= 4:
        c += 1
        init_diametr = curr_diametr

print(c, init_diametr)

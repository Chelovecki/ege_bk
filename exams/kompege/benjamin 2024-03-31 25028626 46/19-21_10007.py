def f(count1, count2, step):
    if count1 + count2 >= 512: return step % 2 == 0
    if step == 0: return 0
    ways = [
        f(count1 + 1, count2, step - 1), f(count1, count2 + 1, step - 1),
        f(count1 + 5, count2, step - 1), f(count1, count2 + 5, step - 1),
        f(count1 * 2, count2, step - 1), f(count1, count2 * 2, step - 1)
    ]
    return any(ways) if step % 2 != 0 else all(ways)


def num_19():
    for x in range(1, 512):
        flag = True
        for y in range(512):
            if f(x, y, 2):
                flag = True
                break
        if flag:
            print("19)", x + y)
            break


def num_20():
    print("20)", [r for r in range(1, 103) if not f(5, r, 1) and f(5, r, 3)])


def num_21():
    print("21)", [r for r in range(1, 52) if not f(10, r, 2) and f(10, r, 4)])


num_19()
num_20()
num_21()

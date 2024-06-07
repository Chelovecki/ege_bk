def f(n):
    def new_f(bin_reperesent: str):
        a, b = bin_reperesent[-2], bin_reperesent[-1]
        if a == b:
            if a == '1':
                bin_reperesent = bin_reperesent[:-2] + a + '0' + b
            else:
                bin_reperesent = bin_reperesent[:-2] + a + '1' + b
        else:
            bin_reperesent = bin_reperesent[:-2] + "".join([str(int(not int(r))) for r in (a, b)])
            bin_reperesent += bin_reperesent[-1]
        return bin_reperesent

    first_loop = new_f(bin(n)[2:])
    second_loop = new_f(first_loop)
    return int(second_loop, 2)


# print(f(12))
# print(f(10))

for n in range(10, 1000):
    res = f(n)
    if res > 168:
        print(n)
        break

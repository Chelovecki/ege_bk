import itertools


def from_10_to(n: int, base):
    res = ''
    while (n != 0):
        res += str(n % base)
        n //= base
    return res[::-1]


def is_palindrome(s: str):
    root = len(s) // 2
    c = 0
    while c <= root:
        if s[c] != s[-1 - c]:
            return 0
        c += 1
    return 1


c = 0
for r in range(1, 1000000):
    good_len = len(from_10_to(r, 7)) <= 7
    endswith_F = hex(r)[2:][-1] == "f"
    check_if_palindrome = is_palindrome(from_10_to(r, 5))
    if check_if_palindrome and endswith_F and good_len:
        c += 1
print(c)

# даже если в ренж добавить еще 1 ноль, то все равно будет 73

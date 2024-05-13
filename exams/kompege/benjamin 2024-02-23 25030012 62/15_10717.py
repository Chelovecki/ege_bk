# подглянул, про невырожденный треуг

def mamax(a, b):
    if a > b:
        return a
    if a <= b:
        return b


def treug(a, b, c):
    return True if a + b > c and b + c > a and a + c > b else False


for a in range(100):
    flag = True
    for x in range(10_0000):
        log_funk = not ((treug(x, 11, 18) == (not (mamax(x, 5) > 68))) and treug(x, a, 5))
        if log_funk is False:
            flag = False
            break
    if flag:
        print(a)
# отв - 64

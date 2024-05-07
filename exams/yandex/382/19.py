A = [1, 2, 3, 0, 6, 5, 4, 8, 7, 9]

s = -1
for i in range(9):
    if A[i] > A[i + 1]:
        A[i + 1] -= A[i]
        s += A[i]
    else:
        A[i + 1] += A[i]
        s -= A[i]

print(s)

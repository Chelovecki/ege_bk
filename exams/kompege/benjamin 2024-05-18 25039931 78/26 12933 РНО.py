data = [list(map(int, r.split())) for r in open('26_12933.txt').readlines()]
N, K = data[0]
data = data[1:]

a = []
for number_detail in range(1, len(data) + 1):
    time_shlifovka = data[number_detail - 1][0]
    time_okras = data[number_detail - 1][1]
    a.append((time_okras, number_detail, 'okras'))
    a.append((time_shlifovka, number_detail, 'slifovka'))

a.sort()

yet_worked = set()
l, r = 1, N
counter = 0
conveer = [0] * (N + 1)

for time, id_detail, type_ in a:
    if id_detail not in yet_worked:
        yet_worked.add(id_detail)

        if type_ == 'okras':
            conveer[r] = id_detail
            r -= 1
        if type_ == 'slifovka':
            counter += 1
            conveer[l] = id_detail
            l += 1

print(counter, conveer[K])

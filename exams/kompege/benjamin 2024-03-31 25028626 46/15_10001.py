for a in range(100):
    if all([((x < y + a) or (x >= 37 - y) or (y <= a)) for x in range(1000) for y in range(1000)]):
        print(a)
        break
# даже если увеличить ренж до 4000 в x и y, то все равно будет
# первый минимальный 12 (правда, надо будет подождать подольше (much more longer...)

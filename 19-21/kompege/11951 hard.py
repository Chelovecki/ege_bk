def get():
    res = []
    words = {"АНТАРКТИДА", "АНТРАЦИТ", "АБАРА", "АБАЖУР", "БББ", "БАОБАБ", "БАР"}
    for n, word in enumerate(zip(list("АНТАРКТИДА"), list("АНТАРКТИДА"), list("АБАРА"), list("АБАЖУР"), list("БББ"), list("БАОБАБ"), list("БАР"))):
        print(word)
        res.append(set([r for r in word]))
    print(res)


get()

def kertaa_kymmenen(alku: int, loppu: int):
    d = {}
    index = alku
    for i in range(alku, loppu+1):
        d[index] = alku * 10
        index += 1
    return d

d = kertaa_kymmenen(2, 7)
print(d)

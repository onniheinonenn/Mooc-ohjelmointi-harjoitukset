
def laske_alkiot(matriisi: list, alkio: int):
    vastaus = 0
    for rivi in matriisi:
        for merkki in rivi:
            if alkio == merkki:
                vastaus += 1 
    return vastaus 
                
m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(laske_alkiot(m, 1))

lista = []

while True:
    luku = int(input('Anna luku: '))
    if luku == 0:
        print('moi')
        break
    lista.append(luku)
    print(f'Lista: {lista}')
    jarjestetty = sorted(lista)
    print(f'Järjestettynä: {jarjestetty}')
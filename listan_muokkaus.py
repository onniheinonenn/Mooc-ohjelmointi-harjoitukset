
lista = []
print('Lista on nyt []')
arvo = 1
while True:
    effect = input('(l)isää, (p)oista vai e(x)it: ')
    if 'e' == effect.lower():
        print('Moi!')
        break

    elif 'l' == effect.lower():
        lista.append(arvo)
        print(f'Lista on nyt {lista}')
        arvo += 1

    elif 'p' == effect.lower():
        lista.pop()
        print(f'Lista on nyt {lista}')
        arvo -= 1


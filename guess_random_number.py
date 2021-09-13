print('Tervetuloa peliin!')

import random

oikea_luku = random.randint(1,10)

yritykset = 0

while True:
    try:
        arvaus = int(input('Arvaa luku väliltä 1-10: '))
        yritykset += 1
    except ValueError:
        print('Ehei! Anna numero.')
        continue

    if arvaus == oikea_luku:
        print('Arvasit oikein, hienoa työtä!')
        break
    if arvaus > oikea_luku:
        print('Annoit liian suuren luvun, yritä uudestaan.')

    if arvaus < oikea_luku:
        print('Annoit liian pienen luvun, yritä uudestaan.')

print('Käytit', yritykset, 'yritystä.')
print('Peli on päättynyt.')

go = [
  [2, 2, 0, 0, 0, 2],
  [2, 0, 0, 1, 0, 2],
  [2, 2, 0, 1, 1, 0],
  [0, 1, 1, 0, 0, 1],
  [0, 1, 2, 1, 1, 1],
  [0, 1, 2, 2, 2, 2],
  [2, 1, 0, 2, 0, 1]
]

def who_won(go: list):
    pelaaja1 = 0
    pelaaja2 = 0
    for row in go:
        for i in row:
            if i == 1:
                pelaaja1 += 1

            if i == 2:
                pelaaja2 += 1

    if pelaaja1 == pelaaja2:
        return 0        
    if pelaaja1 > pelaaja2:
        return 1
    if pelaaja2 > pelaaja1:
        return 2


print(who_won(go))
# https://olimpiada.ic.unicamp.br/pratique/p2/2012/f1/cavalo/
# Solução por Diefesson de Sousa Silva

movimentos = [
    (+0, +0),  # 0
    (+1, +2),  # 1
    (+2, +1),  # 2
    (+2, -1),  # 3
    (+1, -2),  # 4
    (-1, -2),  # 5
    (-2, -1),  # 6
    (-2, +1),  # 7
    (-1, +2),  # 8
]

buracos = [
    (1, 3),
    (2, 3),
    (5, 4),
    (2, 5),
]

_n = input()
passos = map(int, input().split())

x, y = 4, 3
i = 0

for xr, yr in (movimentos[p] for p in passos):
    x, y = x + xr, y + yr
    i += 1
    if (x, y) in buracos:
        break

print(i)

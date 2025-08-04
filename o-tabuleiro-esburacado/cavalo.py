# https://olimpiada.ic.unicamp.br/pratique/p2/2012/f1/cavalo/
# Solução por Diefesson de Sousa Silva

# Tabela de movimentos
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

# Lista de buracos
buracos = [
    (1, 3),
    (2, 3),
    (5, 4),
    (2, 5),
]

_n = input() # Como essa variável não é usada adicionamos _
passos = map(int, input().split())

x, y = 4, 3
contagem = 0

# Simula cada passo
for xr, yr in (movimentos[p] for p in passos):
    x, y = x + xr, y + yr
    contagem += 1
    # Para ao cair em um buraco
    if (x, y) in buracos:
        break

print(contagem)

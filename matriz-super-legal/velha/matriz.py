# https://olimpiada.ic.unicamp.br/pratique/pu/2019/f2/matriz/
# Solução por Diefesson de Sousa Silva


def inicia_legais(l, c):
    return [
        [
            [[False for _c2 in range(c - c1 - 1)] for c1 in range(c - 1)]
            for _l2 in range(l - l1 - 1)
        ]
        for l1 in range(l - 1)
    ]


def indices(l1, l2, c1, c2):
    li1 = l1
    li2 = l2 - l1 - 1
    ci1 = c1
    ci2 = c2 - c1 - 1
    return li1, li2, ci1, ci2


def obter_legal(legais, l1, l2, c1, c2):
    li1, li2, ci1, ci2 = indices(l1, l2, c1, c2)
    return legais[li1][li2][ci1][ci2]


def definir_legal(legais, l1, l2, c1, c2, valor):
    li1, li2, ci1, ci2 = indices(l1, l2, c1, c2)
    legais[li1][li2][ci1][ci2] = valor


def testa_elemento(matriz, l1, l2, c1, c2):
    return matriz[l1][c1] + matriz[l2][c2] <= matriz[l1][c2] + matriz[l2][c1]


l, c = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(l)]
maior = 0


legais = inicia_legais(l, c)

for l1 in range(l - 1):
    for l2 in range(l1 + 1, l):
        for c1 in range(c - 1):
            for c2 in range(c1 + 1, c):
                cima_ok = c2 - 1 == c1 or obter_legal(legais, l1, l2, c1, c2 - 1)
                esquerda_ok = l2 - 1 == l1 or obter_legal(legais, l1, l2 - 1, c1, c2)
                elemento_ok = testa_elemento(matriz, l1, l2, c1, c2)
                if cima_ok and esquerda_ok and elemento_ok:
                    definir_legal(legais, l1, l2, c1, c2, True)
                    tamanho = (l2 - l1 + 1) * (c2 - c1 + 1)
                    if tamanho > maior:
                        maior = tamanho

print(maior)

# https://olimpiada.ic.unicamp.br/pratique/pu/2019/f1/chuva/
# Solução por Diefesson de Sousa Silva

SECO = "."
MOLHADO = "o"
PRATELEIRA = "#"


# Funções de utilidade
def nos_limites(i, j):
    return 0 <= i < linhas and 0 <= j < colunas


def obter(i, j):
    if nos_limites(i, j):
        return parede[i][j]
    else:
        return None


linhas, colunas = map(int, input().split())
parede = [list(input()) for _ in range(linhas)]

# Busca o ponto inicial molhado
for j in range(colunas):
    if parede[0][j] == MOLHADO:
        ponto_inicial = (0, j)
        break

# Uma estrutura de "pilha" nos permite trabalhar de forma depth first sem resultar em um stack overflow
pilha = [ponto_inicial]

while len(pilha) > 0:
    i, j = pilha.pop()
    # Se houver uma prateleira embaixo, espalhar para os lados
    if obter(i + 1, j) == PRATELEIRA:
        # Esquerda
        if obter(i, j - 1) == SECO:
            parede[i][j - 1] = MOLHADO
            pilha.append((i, j - 1))
        # Direita
        if obter(i, j + 1) == SECO:
            parede[i][j + 1] = MOLHADO
            pilha.append((i, j + 1))
    # Baixo
    elif obter(i + 1, j) == SECO:
        parede[i + 1][j] = MOLHADO
        pilha.append((i + 1, j))


for l in parede:
    print("".join(l))

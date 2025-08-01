# https://olimpiada.ic.unicamp.br/pratique/pu/2019/f2/matriz/
# Solução por Diefesson de Sousa Silva

n_linhas, n_colunas = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(n_linhas)]

# n_linhas, n_colunas = 2, 2
# matriz = [[1, 5], [5, 1]]


legal = [[False for _ in range(n_colunas)] for _ in range(n_linhas)]
altura = [[0 for _ in range(n_colunas)] for _ in range(n_linhas)]
esquerda = [[-1 for _ in range(n_colunas)] for _ in range(n_linhas)]
direita = [[-1 for _ in range(n_colunas)] for _ in range(n_linhas)]

# Encontra todas as matrizes 2x2 legais
for i in range(n_linhas - 1):
    for j in range(n_colunas - 1):
        legal[i][j] = (
            matriz[i][j] + matriz[i + 1][j + 1] <= matriz[i + 1][j] + matriz[i][j + 1]
        )

# Altura do grupo de submatrizes legais
for i in range(n_linhas - 1):
    for j in range(n_colunas - 1):
        if legal[i][j]:
            altura[i][j] = 1 if i == 0 else 1 + altura[i - 1][j]

# Coluna mais a esquerda de altura maior ou igual (inclusivo)
for i in range(n_linhas - 1):
    # Usamos uma "pilha" para evitar uma busca linear
    anteriores = []  # Tuplas de (indice da coluna, altura)
    for j in range(n_colunas - 1):
        while len(anteriores) > 0 and anteriores[-1][1] >= altura[i][j]:
            anteriores.pop()
        if len(anteriores) == 0:
            esquerda[i][j] = 0
        else:
            esquerda[i][j] = anteriores[-1][0] + 1
        anteriores.append((j, altura[i][j]))

# Coluna mais a direita de altura maior ou igual (exclusivo)
for i in range(n_linhas - 1):
    anteriores = []
    for j in range(n_colunas - 2, -1, -1):
        while len(anteriores) > 0 and anteriores[-1][1] >= altura[i][j]:
            anteriores.pop()
        if len(anteriores) == 0:
            direita[i][j] = n_colunas - 1
        else:
            direita[i][j] = anteriores[-1][0]
        anteriores.append((j, altura[i][j]))


# Calcula e exibe solução
maior = 0
for i in range(n_linhas - 1):
    for j in range(n_colunas - 1):
        if legal[i][j]:
            maior = max(maior, (direita[i][j] - esquerda[i][j] + 1) * (altura[i][j] + 1))

print(maior)

# https://olimpiada.ic.unicamp.br/pratique/p1/2018/f1/xadrez/
# Solução por Diefesson de Sousa Silva

l = int(input())
c = int(input())

cor = int((l + c) % 2 == 0)

print(cor)

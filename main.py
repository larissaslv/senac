import aleatorio
'''
# as al -> apelido para a biblioteca aleatorio


ini,fim = al.fn_consiste_num()
print(f"O intervalo é entre {ini} e {fim} ")


import aleatorio

# consiste inicio e fim do intervalo
ini, fim = aleatorio.fn_consiste_num()

# chama função para exibir um número aleatório no intervalo
print("Exibe um número aleatório")
aleatorio.fn_def_aleatorio(ini,fim)

# pula uma linha
print()

# Lê quantidade de números aleatorios a exibir
qtd = 100
while qtd < 1 or qtd > 99:
    qtd = int(input("Quantidade entre 1 e 99:"))
    if qtd < 1 or qtd > 99: print("ERRO - Fora do intervalo")

# consiste inicio e fim do intervalo
ini, fim = aleatorio.fn_consiste_num()

# chama função para exibir uma lista de números aleatórios
'''

#aleatorio.numero_aleatorio()
aleatorio.fn_soma()

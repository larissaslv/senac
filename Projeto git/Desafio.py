import random
"""
Fazer no programa jogos.py, a função fn_estatisticas que:
-> le o arquivo com os jogos da megasena
-> exiba, na tela: Quantos jogos foram lidos
Quantas vezes cada n° apareceu nos jogos
Qual o percentual de cada número.
"""
def fn_estatistica():
    arq=open("megasena.txt",'r')
    qtd_em_str_jogos=arq.readlines()# Estou lendo toda a lista a lista e jogando no qtd_em_str_jogos.
    lista_quant_dez = [0] * 60 # A lista começa no zero e mostra toda onde cada elemento está.
    print("Dezenas lidas: ")# Vai mostrar no programa as dezenas q foram lidas.
    for linha in qtd_em_str_jogos:
        qtd_em_str_jogos = linha.split(", ")# o split localiza o (", ") ele vai desabilitar
        qtd_num_linha = [] # lista q vai armazenar os números inteiros.
        for num_str in qtd_em_str_jogos:
            qtd_num_linha.append(int(num_str))
        print(qtd_num_linha)
        for dezena in qtd_num_linha:
            lista_quant_dez[dezena] += 1

    arq.close()
def fn_lista():
    acesso=[0]*10
    for indice in range (10):
        acesso[indice]= random.randit(1,100)
    for indice in range (10):
        print(str(indice) + ": " + str(acesso[indice]))
    print("lista", acesso)




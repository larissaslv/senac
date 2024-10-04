import random
"""
Construir o programa jogos.py

"""
lista_dez=[]# VAi gerar números de 1 a 10.
def geranum():
    print("6 dezenas aleatórias", end='')
    numeros = random.sample(range(60),6)
    print(numeros)

    """
      num=random.sample(59)
    num=int(input("Digite um número de 1 a 59: "))
    lista_dez.append(num)
    print(random.sample(lista_dez,k))
    :return: 
    """


"""
Construir uma função que crie o arquivo megasena.txt
leia, via teclado, a quantidade de números a serem gerados entre 1 e 100.
gravar esses n° no arquivo, gerados aleatoriamente e sem repetição.
"""
def fn_arqmega ():
    arq=open("megasena.txt",'a')# o python cria o arquivo megasena.txt. Ele vai gravar os números no arquivo megasena.txt
    listar_arq=[] # vai receber todos os sorteios
   # print("Digite a quantidade de números para serem gerados entre 1 e 100. ")
   # ct_linha= 0; linha=''
    qtd_jogos=int(input("Quantidade de jogos: "))
    """while ct_linha < 100:
        ct_linha += 1
    print('numeros' + str, (ct_linha), end='' )
    linha="1234" """
    for ct_jogos in range (qtd_jogos):
        lista_mega=[]
        lista_mega.append(random.sample(range(60),6))# O range cria uma sequencia de 0 a 56 e pega       aleatoriamente 6 deles.
        string_mega = ','.join(map(str,lista_mega))# Aqui é uma combinação de 3 comandos. nesse comando -> (map(str,lista_mega), o map vai passar para string (str) todos os valores da (lista_ mega).              Os elementos que serão convertidos em string, precisam ser separados por algo e aí entra o comando (.join)
        listar_arq.append(string_mega + "\n")# VAi ser inserido no final da lista (listar_arq) a lista (string_mega)
    arq.writelines(listar_arq)# Aqui vai pegar a lista e jogar no arquivo.
    # o writelines vai
    arq.close()

def fn_listamega():
    arq = open("megasena.txt", "r")
    lista_str_mega = arq.readlines()
    for linha in lista_str_mega:
        lista_str_linha = linha.split(", ")# o split localiza o (", ") ele vai desabilitar
        lista_num_linha = []
        for num_str in lista_str_linha:
            lista_num_linha.append(int(num_str))
        print(lista_num_linha)
    arq.close()
# comando .split->
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

import random
import Consistencias
import Cores
import datetime
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

def fn_professor():
    Cores.fn_cor_texto("PRETO", "LILAS", "PROFESSOR....", 1)
    Cores.fn_cor_texto("PRETO", "LILAS", "....CORUJINHA", 1)
    termo1 = random.randint(3,999)
    termo2 = random.randint(1, termo1 - 1)
    oper = random.randint(1,2)
    Cores.fn_cor_texto("PRETO", "VERDE", "  " + f"{termo1:03d}", 0)
    if oper == 1:
        Cores.fn_cor_texto("PRETO", "VERMELHO", " + ", 0)
        res = termo1 + termo2
    else:
        Cores.fn_cor_texto("PRETO", "VERMELHO", " - ", 0)
        res = termo1 - termo2
    Cores.fn_cor_texto("PRETO", "VERDE", f"{termo2:03d}" + "  ", 1)
    jogada = 0; ct_erro = 0
    while ct_erro < 5 and jogada != res:
        jogada = Consistencias.fn_consiste_int(0,999,"Digite o resultado")
        if jogada < (res - 15) or jogada > (res + 15):
            Cores.fn_cor_texto("PRETO", "AMARELO", "TÁ FRIO......", 1)
        elif jogada < (res - 10) or jogada > (res + 10):
            Cores.fn_cor_texto("PRETO", "AMARELO", "TÁ MORNO...", 1)
        elif jogada < (res - 5) or jogada > (res + 5):
            Cores.fn_cor_texto("PRETO", "AMARELO", "TÁ QUENTE....", 1)
        else: Cores.fn_cor_texto("PRETO", "AMARELO", "TÁ FERVENDO..", 1)
        if jogada != res:
            ct_erro += 1
#            fn_erro(ct_erro)
    if ct_erro == 5: Cores.fn_cor_texto("PRETO", "VERMELHO", "ENFORCADO !!!", 1)
    else: Cores.fn_cor_texto("PRETO", "VERDE", "PARABENS  !!!", 1)

#=====================================================================================================
# lin = linha e col = colun
def fn_tabuleiro (lista_tab):
    lista_abc = ["A  ", "B  ", "C  "]
    Cores.fn_cor_texto('Preto', 'Amarelo', 'TABULEIRO', 1)

    conta_lista = 0

    for conta_linha in range(3):
        Cores.fn_cor_texto('PRETO', 'AMARELO', lista_abc[conta_linha], 0)
        for conta_coluna in range(3):
            Cores.fn_cor_texto('PRETO', 'AZUL', lista_tab[conta_lista] + "  ", 0)
            conta_lista += 1 # Conta a lista para sempre avançar para a proxima posição
        Cores.fn_cor_texto('PRETO', 'AZUL', " ", 1)
    Cores.fn_cor_texto('PRETO', 'AMARELO', '   1  2  3   ', 1)

def fn_joga_humano(lista_tab):
    Cores.fn_cor_texto('PRETO', 'AMARELO', 'HUMANO JOGA  ', 1)
    lista_jogo = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    coordenadas = ""
    while len(coordenadas) != 2:
        coordenadas = input("Coordenadas:")
        if len(coordenadas) == 2:
            if 'A' <= coordenadas[0] <= 'C':
                if '1' <= coordenadas[1] <= '3':
                    if lista_tab[lista_jogo.index(coordenadas)] == '-':
                        lista_tab[lista_jogo.index(coordenadas)] = 'X'
                    else:
                        print("ERRO! - Coordenada já foi jogada")
                        coordenadas = ""
                else:
                    print("ERRO! - Coluna inválida")
                    coordenadas = ""
            else:
                print("ERRO! - Linha inválida")
                coordenadas = ""
        else:
            print("ERRO - Apenas linha e coluna válidos")
            coordenadas = ""
    return lista_tab

def fn_joga_computador(lista_tab):
    Cores.fn_cor_texto('PRETO', 'AMARELO', 'COMPUTADOR   ', 1)
    jogada = -1
    while jogada < 0:
        jogada = random.randint(0, 8)
        if lista_tab[jogada] == '-': lista_tab[jogada] = 'O'
        else: jogada = -1
    return lista_tab

def fn_jogadas_velha(apelido):
    lista_tab = ['-'] * 9
    conta_jogadas_comp= 0
    conta_jogadas_hum= 0
    Cores.fn_cor_texto('PRETO', 'AMARELO', ' JOGO DA VELHA ', 1)
    Cores.fn_cor_texto('Preto', 'VERDE' ,    '|' '--' '|' '--' '|' '--' '|',1)
    Cores.fn_cor_texto('Preto', 'VERDE' ,    '|' '--' '|' '--' '|' '--' '|',1)
    Cores.fn_cor_texto('Preto', 'VERDE' ,    '|' '--' '|' '--' '|' '--' '|', 1)
    Cores.fn_cor_texto('PRETO', 'AMARELO', ' COORDENADAS: A1, A2, A3, B1, B2, B3, C1, C2, C3', 1)
    sorteio = random.randint(1,2)
    if sorteio == 1: letra = 'X'
    else: letra = 'O'
    ct_jogada = 0
    while ct_jogada < 9:
        if letra == 'X':
            conta_jogadas_hum += 1
            print()
            lista_tab = fn_joga_humano(lista_tab)
            if ver_vencedor('X', lista_tab):
                Cores.fn_cor_texto('PRETO', 'VERMELHO', 'VOCÊ VENCEU', 1)
                ct_jogada = 9
            letra = 'O'
        else:
            conta_jogadas_comp += 1
            print()
            lista_tab = fn_joga_computador(lista_tab)
            if ver_vencedor('O', lista_tab):
                Cores.fn_cor_texto('PRETO', 'VERMELHO', 'COMPT. VENCEU', 1)
                ct_jogada = 9
            letra = 'X'
        fn_tabuleiro(lista_tab)
        ct_jogada += 1
    hora_formatada = datetime.datetime.now().strftime('%Y-%m-%d %H:%M') #esse comando strtime deixa no formato (ano,mês,dia, hora e minuto) ignorando os segundos.
    Cores.fn_cor_texto('PRETO', 'AMARELO', hora_formatada, 1)
    Cores.fn_cor_texto('PRETO','VERDE','Você fez '+ str(conta_jogadas_hum),'jogadas')
    Cores.fn_cor_texto('PRETO','AZUL', "Eu fiz " + str(conta_jogadas_comp), "jogadas")
    print("FIM !")

def ver_vencedor(letra, lista_tab):
    # Para verificar o acerto por linhas
    for lin in range (3):
        ct_igual=0
        for col in range (3):
            indice = col + 3 * lin # Vai verificar se tem
            if lista_tab[indice] == letra:
                ct_igual += 1
        if ct_igual == 3:
            return True
# Para verificar o acerto por colunas
    for col in range(3):
        ct_igual = 0
        for lin in range(3):
            indice = col + 3 * lin  # Cálculo do índice para coluna
            if lista_tab[indice] == 'X':
                ct_igual += 1
            if ct_igual == 3:
                return True  # Vitória encontrada

# Verificar diagonais
    if lista_tab[0] == 'X' and lista_tab[4] == 'X' and lista_tab[8] == 'X':
        return True  # Diagonal principal
    if lista_tab[2] == 'X' and lista_tab[4] == 'X' and lista_tab[6] == 'X':
        return True  # Diagonal secundária

    return False  # Nenhuma vitória encontrada
'''
def fn_estrategia(lista_tab, let):
        coordenada = -1
        for c in range(3):
            i = 3 * c
            if lista_tab[0 + i] == '-' and lista_tab[1 + i] == let and lista_tab[2 + i] == let: coordenada = 0 + i
            if lista_tab[0 + i] == let and lista_tab[1 + i] == '-' and lista_tab[2 + i] == let: coordenada = 1 + i
            if lista_tab[0 + i] == let and lista_tab[1 + i] == let and lista_tab[2 + i] == '-': coordenada = 2 + i
            if lista_tab[0 + c] == '-' and lista_tab[3 + c] == let and lista_tab[6 + c] == let: coordenada = 0 + c
            if lista_tab[0 + c] == let and lista_tab[3 + c] == '-' and lista_tab[6 + c] == let: coordenada = 3 + c
            if lista_tab[0 + c] == let and lista_tab[3 + c] == let and lista_tab[6 + c] == '-': coordenada = 6 + c
        if lista_tab[0] == '-' and lista_tab[4] == let and lista_tab[8] == let: coordenada = 0
        if lista_tab[0] == let and lista_tab[4] == '-' and lista_tab[8] == let: coordenada = 4
        if lista_tab[0] == let and lista_tab[4] == let and lista_tab[8] == '-': coordenada = 8
        if lista_tab[2] == '-' and lista_tab[4] == let and lista_tab[6] == let: coordenada = 2
        if lista_tab[2] == let and lista_tab[4] == '-' and lista_tab[6] == let: coordenada = 4
        if lista_tab[2] == let and lista_tab[4] == let and lista_tab[6] == '-': coordenada = 6
        return coordenada
        
'''

def fn_estrategia(lista_tab, let):
    coordenada = -1

    # Definindo todas as combinações vencedoras (linhas, colunas e diagonais)
    combinacoes_vencedoras = [
        (0, 1, 2),  # Linha 1
        (3, 4, 5),  # Linha 2
        (6, 7, 8),  # Linha 3
        (0, 3, 6),  # Coluna 1
        (1, 4, 7),  # Coluna 2
        (2, 5, 8),  # Coluna 3
        (0, 4, 8),  # Diagonal principal
        (2, 4, 6)   # Diagonal secundária
    ]

    # Loop por cada combinação vencedora
    for comb in combinacoes_vencedoras:
        a, b, c = comb
        # Verifica se há uma oportunidade para ganhar ou bloquear
        if lista_tab[a] == '-' and lista_tab[b] == let and lista_tab[c] == let:
            coordenada = a
        elif lista_tab[a] == let and lista_tab[b] == '-' and lista_tab[c] == let:
            coordenada = b
        elif lista_tab[a] == let and lista_tab[b] == let and lista_tab[c] == '-':
            coordenada = c

    return coordenada

def fn_relatorios_velha(apelido):
    try:
        arq = open("jogadas.txt", "r")
        lista_arq = arq.readlines()
    except:
        arq = open("jogadas.txt", "w")
        lista_arq = []
    arq.close()
    lista_apelido = []; lista_tot_vitorias = []; lista_tot_empates = []; lista_tot_derrotas = []
    while True:
        print("Menu do Jogo da Velha - Relatórios")
        print("1. Quem mais Ganhou")
        print("2. Quem mais perdeu")
        print("3. Minhas estatísticas")
        print("0. Volta para o Menu do Jogo da Velha")
        opcao1 = input("Escolha uma opção: ")
        if opcao1 == '1':   print("Não existo ainda")
        elif opcao1 == '2': print("Não existo ainda")
        elif opcao1 == '3': print("Não existo ainda")
        elif opcao1 == '0': break
        else: print("ERRO - Opção inválida!")

def fn_jogo_da_velha():
    try:
        arq = open("jogadores.txt", "r")
        lista_arq = arq.readlines()
    except:
        arq = open("jogadores.txt", "w")
        lista_arq = []
    arq.close()
    segue = 1
    while segue:
        apelido = input("Apelido entre 5 e 10 caracteres:")
        if len(apelido) < 5 or len(apelido) > 10:
            print("ERRO - Somente entre 5 e 10 caracteres")
        else:
            ap_quebra_linha = apelido + "\n"
            if ap_quebra_linha in lista_arq: # Certo
                 while True:
                    print("Jogo da Velha -> Menu do Jogo da Velha")
                    print("1. Jogar")
                    print("2. Relatorios")
                    print("0. Volta para o menu Jogo da Velha")
                    opcao1 = input("Escolha uma opção: ")
                    if opcao1 == '1':
                        continua = 1
                        while continua == 1:
                            fn_jogadas_velha(apelido)
                            continua = Consistencias.fn_consiste_int(1,2,"Continua 1(sim) 2(não)")
                    elif opcao1 == '2': fn_relatorios_velha(apelido)
                    elif opcao1 == '0': break
                    else: print("ERRO - Opção inválida!")
            else:
                fn_jogadas_velha(apelido)
                lista_arq.append(ap_quebra_linha)
            segue = 0

    arq = open("jogadores.txt", "w")
    arq.writelines(lista_arq)
    arq.close()






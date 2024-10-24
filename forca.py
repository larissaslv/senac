import Cores
import random
import Consistencias
def chama_boneco0():
    Cores.fn_cor_texto("PRETO", "VERDE", "     (¨)     ", 1)
    Cores.fn_cor_texto("PRETO", "VERDE", "   *==|==*   ", 1)
    Cores.fn_cor_texto("PRETO", "VERDE", "      |      ", 1)
    Cores.fn_cor_texto("PRETO", "VERDE", "     / \     ", 1)
    Cores.fn_cor_texto("PRETO", "VERDE", "    |   |    ", 1)
def chama_boneco1():
    Cores.fn_cor_texto("PRETO", "VERDE", "     (¨)     ", 1)
    Cores.fn_cor_texto("PRETO", "VERDE", "   *==|==*   ", 1)
    Cores.fn_cor_texto("PRETO", "VERDE", "      |      ", 1)
    Cores.fn_cor_texto("PRETO", "VERDE", "     / \     ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", " |   |    ", 1)
def chama_boneco2():
    Cores.fn_cor_texto("PRETO", "VERDE", "        (¨)     ", 1)
    Cores.fn_cor_texto("PRETO", "VERDE", "      *==|==*   ", 1)
    Cores.fn_cor_texto("PRETO", "VERDE", "         |      ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "     / \     ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "    |   |    ", 1)
def chama_boneco3():
    Cores.fn_cor_texto("PRETO", "VERDE", "        (¨)     ", 1)
    Cores.fn_cor_texto("PRETO", "VERDE", "      *==|==*   ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "      |      ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "     / \     ", 1)
    Cores.fn_cor_texto("PRETO", "VERMLEHO", "    |   |    ", 1)
def chama_boneco4():
    Cores.fn_cor_texto("PRETO", "VERDE", "        (¨)     ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "   *==|==*   ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "      |      ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "     / \     ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "    |   |    ", 1)
def chama_boneco5():
    Cores.fn_cor_texto("PRETO", "VERMELHO", "     (¨)     ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "   *==|==*   ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "      |      ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "     / \     ", 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "    |   |    ", 1)


def fn_erro(conta_erro):
    if conta_erro == 0: chama_boneco0()
    if conta_erro == 1: chama_boneco1()
    if conta_erro == 2: chama_boneco2()
    if conta_erro == 3: chama_boneco3()
    if conta_erro == 4: chama_boneco4()
    if conta_erro == 5: chama_boneco5()
'''
def fn_forca():
    Cores.fn_cor_texto("PRETO", "AZUL", "JOGO DA FORCA", 1)
    chama_boneco0()
    conta_erro=0; conta_acerto=0
    fn_erro(conta_erro)
    try: arq = open("Palavras.txt", "r") # Tentar abrir o arquivo em modo leitura
    except:
        print("ERRO - Arquivo Palavras.txt não pode ser aberto !") # Se a palavra não existir no arquivo gera esse erro.
        return
    lista_letras=""
    lista_palavras = arq.readlines()
    letras_jogadas = ""
    lista_deletras = ['*', '*', '*', '*', '*']
    lista_pos= ['#','#','#','#','#']
    sorteio = random.randint(1,len(lista_palavras)) # Vai sortear as palavras aleatoriamente por conta do random.
    palavra = lista_palavras[sorteio - 1][0:5] # Palavra recebe lista de palavras.
    for tentativa in range(10):  # Limite de 10 tentativas (erros + acertos)
      if conta_erro >= 5 or conta_acerto >= 5:
        break  # Sai do loop se o limite de erros ou acertos for atingido
    print("ERRO: " + str(conta_erro) + "   ACERTO: " + str(conta_acerto))
    letra = input("Adivinhe a letra:")


    if len(letra) != 1 or letra < 'a' or letra > 'z':
        print("ERRO - Somente uma letra minúscula!")
    elif letra in letras_jogadas:
        print("ERRO - Essa letra já foi jogada!")
    elif not (letra in palavra):
        conta_erro += 1
    else:
        for conta in range(len(palavra)):
            if letra == palavra[conta]:
                lista_deletras[conta] = letra
                conta_acerto += 1
        letras_jogadas += letra
        print("Letra na posição correta:", lista_letras)
        print ("Posição incorreta: ", lista_pos)
'''
def fn_forca():
    Cores.fn_cor_texto("PRETO", "AZUL", "JOGO DA FORCA", 1)
    chama_boneco0()
    conta_erro=0; conta_acerto=0
    fn_erro(conta_erro)
    try: arq = open("Palavras.txt", "r") # Tentar abrir o arquivo em modo leitura
    except:
        print("ERRO - Arquivo Palavras.txt não pode ser aberto !") # Se a palavra não existir no arquivo gera esse erro.
        return
    lista_letras=""
    lista_palavras = arq.readlines()
    letras_jogadas = ""
    lista_deletras = ['*', '*', '*', '*', '*']
    lista_posicao= ['#','#','#','#','#']
    sorteio = random.randint(1,len(lista_palavras)) # Vai sortear as palavras aleatoriamente por conta do random.
    palavra = lista_palavras[sorteio - 1][0:5] # Palavra recebe lista de palavras.
    for tentativa in range(10):  # Limite de 10 tentativas (erros + acertos)
      if conta_erro >= 5 or conta_acerto >= 5:
        break  # Sai do loop se o limite de erros ou acertos for atingido
    print("ERRO: " + str(conta_erro) + "   ACERTO: " + str(conta_acerto))
    letra = input("Adivinhe a letra:")


    if len(letra) != 1 or letra < 'a' or letra > 'z':
        print("ERRO - Somente uma letra minúscula!")
    elif letra in letras_jogadas:
        print("ERRO - Essa letra já foi jogada!")
    elif not (letra in palavra):
        conta_erro += 1
    else:
        for conta in range(len(palavra)):
            if letra == palavra[conta]:
                lista_deletras[conta] = letra
                conta_acerto += 1
        letras_jogadas += letra
        print("Letra na posição correta:", lista_letras)
        print ("Posição incorreta: ", lista_posicao)

def fn_joga():
    lista_jogo = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    coordenadas = ""; letra = ""; posicao = 0
    while len(coordenadas) != 2:

        coordenadas = input("Coordenadas:").upper()
        if len(coordenadas) == 2:
            if 'A' <= coordenadas[0] <= 'Z':
                if '1' <= coordenadas[1] <= '5':
                    letra = coordenadas [0]
                    posicao = int(coordenadas[1])

                else:
                    print("ERRO! - Posição inválida")
                    coordenadas = ""
            else:
                print("ERRO! - Letra inválida")
                coordenadas = ""
        else:
            print("ERRO - Digite uma letra e uma posição válidos")
            coordenadas = ""
    return coordenadas, letra, posicao

def fn_palavra():
    lista_pal=[]
    try:
        arq=open("Palavras.txt", "r")
        lista_arq=arq.readlines()

    except:
        arq=open("Palavras.txt", "w")
        lista_arq=[]
    for linha in lista_arq:
        lista_linha = linha.split("][")
        lista_pal.append(lista_linha[0])

    arq.close()
    return lista_pal



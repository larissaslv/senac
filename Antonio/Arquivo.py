
def fn_w_arq():
    arq = open("arq.txt", "a")
    lista_arq = []
    print("Escreva palavras com 5 letras, separando-as com <Enter>");
    print("Cadastre no máximo 9 palavras")
    print("Para terminar o cadastro, digite KABô!")
    ct_linha = 0; linha=""
    while linha != "KABÔ!" and ct_linha < 9:
        ct_linha += 1
        print("Linha " + str(ct_linha), end=": ")
        linha = "123456"
        while len(linha) != 5:
            linha = input()
            if len(linha) != 5: print("Digite somente palavra com 5 letras: ",end="")
        if linha != "KABÔ!": lista_arq.append(linha + "\n")
    print("salvando o arquivo arq.txt")
    arq.writelines(lista_arq)
    print("arq.txt foi salvo")
    arq.close()

def fn_texto_a_arq():
    arq = open("texto.txt", "a")
    lista_arq = []
    print("Escreva frases com até 100 letras, separando-as com <Enter>");
    print("Cadastre no máximo 99 palavras")
    print("Para terminar o cadastro, digite KABô!")
    ct_linha = 0; linha=""
    while linha != "KABÔ!" and ct_linha < 99:
        ct_linha += 1
        print("Linha " + str(ct_linha), end=": ")
        linha = "01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
        while len(linha) > 100:
            linha = input()
            if len(linha) > 100:
                print("Digite somente frase com até 100 letras: ",end="")
        if linha != "KABÔ!": lista_arq.append(linha + "\n")
    print("salvando o arquivo texto.txt")
    arq.writelines(lista_arq)
    print("texto.txt foi salvo")
    arq.close()

def fn_r_arq():
    vogais = "aeiouAEIOU"
    arq = open("arq.txt", "r")
    lista_arq = []; ct_linha = 0
    print("Conteúdo do arquivo arq.txt")
    lista_arq = arq.readlines()
    for linha in lista_arq:
        ct_linha += 1; ct_vogais = 0
        for letra in linha:
            if letra in vogais: ct_vogais += 1
        print(str(ct_linha)+". Vogais:"+str(ct_vogais)+" Palavra: "+linha, end="")
    arq.close()

def fn_texto_r_arq():
    vogais = "aeiouAEIOU"
    arq = open("texto.txt", "r")
    lista_arq = [];
    ct_linha = 0
    print("Conteúdo do arquivo texto.txt")
    lista_arq = arq.readlines()
    for linha in lista_arq:
        ct_linha += 1;
        ct_vogais = 0
        for letra in linha:
            if letra in vogais: ct_vogais += 1
        print(str(ct_linha) + ". Vogais:" + str(ct_vogais) + " Frase: " + linha, end="")
    arq.close()

def fn_texto_r_arq():
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpkrstvwxyzBCDFGHJKLMNPKRSTVWXYZ"
    contvogais="a","A,","e","E","i","I","o","O","u","U"
    arq = open("texto.txt", "r")
    lista_arq = [];
    ct_linha = 0
    print("Conteúdo do arquivo texto.txt")
    lista_arq = arq.readlines()
    for linha in lista_arq:
        ct_linha += 1;
        ct_vogais = 0
        ct_consoantes = 0
        ct_contvoagais = 0
        for letra in linha:
            if letra in vogais: ct_vogais += 1
            elif letra in vogais: ct_consoantes +=1
            elif letra in vogais: ct_contvoagais +=1
        print(str(ct_linha) + ". Vogais:" + str(ct_vogais) + "Consoantes: " + str(ct_consoantes) + "Número de vogais: "+str(ct_contvoagais)+" Frase: " + linha, end="")
    arq.close()

#Solução do professor:
"""
def fn_texto_r_arq():
    vogais = "aeiou"
    consoa = "bcdfghjklmnpqrstvxywz"
    arq = open("texto.txt", "r")
    lista_arq = []
    ct_linha = 0
    print("Conteúdo do arquivo texto.txt")
    lista_arq = arq.readlines()
    for linha in lista_arq:
        linha_ant = linha
        linha = linha.lower()
        ct_linha += 1
        ct_vogais = 0
        ct_consoa = 0
        ct_a = 0; ct_e = 0; ct_i = 0; ct_o = 0; ct_u = 0
        for letra in linha:
            if letra in vogais: ct_vogais += 1
            if letra in consoa: ct_consoa += 1
            if letra == 'a': ct_a += 1
            if letra == 'e': ct_e += 1
            if letra == 'i': ct_i += 1
            if letra == 'o': ct_o += 1
            if letra == 'u': ct_u += 1
        print(str(ct_linha), end=".")
        print("Vogais:" + str(ct_vogais), end="  ")
        print("a:" + str(ct_a) + "  e:" + str(ct_e) + "  i:" + str(ct_i), end="  ")
        print("o:" + str(ct_o) + "  u:" + str(ct_u), end="  ")
        print("Consoantes:" + str(ct_consoa))
        print("- Frase: " + linha_ant, end="")
    arq.close()

"""

#No programa Arquivos.py, fazer uma função chamada fn_seleciona que:
#O usuário digita uma palavra de 5 letras.
#A função procura no arquivo de palavras se ela existe.
#Se existir, exiba a posição dela no arquivo.
#Senão exiba a mensagem "Não achei!"
#Permitir que o usuário digite nova palavra para pesquisar.
#Caso o usuário digite "!", a função termina.

#def fn_seleciona ():

'''
    palav= (input("Digite uma palavra de 5 letras: "))
    arq = open("texto.txt", "r") # Vai procurar a palavra
    lista_arq = [] # Lista que recebeu as palavras do arquivo.
    ct_linha = 0 # contador de linha
    proc= 0
    while proc <5 or proc >5:
        print ("Digite uma palavra de até 5 letras para procurar ")
        break
    i=lista_arq.index(palav)
    print(f"Sua palavra está{i}")
    '''
def fn_seleciona():
    while True:
        palavra = input("Digite uma palavra de 5 letras (ou '!' para sair): ")

        # Verifica se o usuário deseja sair
        if palavra == "!":
            print("Saindo do programa...")
            break

        # Verifica se a palavra tem exatamente 5 letras
        if len(palavra) != 5:
            print("A palavra deve ter exatamente 5 letras.")
            continue

        # Abre o arquivo e procura pela palavra
        try:
            with open("texto.txt", "r") as arq:
                encontrado = False
                for i, linha in enumerate(arq):
                    palavras_linha = linha.split()
                    if palavra in palavras_linha:
                        print(f"A palavra '{palavra}' foi encontrada na linha {i + 1}.")
                        encontrado = True
                        break

                if not encontrado:
                    print("Não achei!")

        except FileNotFoundError:
            print("O arquivo 'texto.txt' não foi encontrado.")







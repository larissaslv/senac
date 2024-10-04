def fn_w_arq():# O w escreve, então aqui o programa vai escrever.
    arq = open("arq.txt", "a")
    lista_arq = []
    print("Escreva palavras com 5 letras, separando-as com <Enter>")
    print("Cadastre no máximo 9 palavras")
    print("Para terminar o cadastro, digite KABÔ!")
    ct_linha = 0; linha="" # ct_linha recebe 0 e linha recebe vazio. vou precisar linnha vazia pois para entrar no while ela precisa exitir previamente.
    while linha != "KABÔ!" and ct_linha < 9:
        ct_linha += 1
        print("Linha " + str(ct_linha), end=": ")
        linha = "123456"
        while len(linha) != 5: # len linha diferente de 5 entra no while.
            linha = input()
            if len(linha) != 5: print("Digite somente palavra com 5 letras: ",end="") # quando o usuário entra com um dígito igual a 5, ele sai do while e entra no if abaixo.
        if linha != "KABÔ!": lista_arq.append(linha + "\n")
    print("salvando o arquivo arq.txt")
    arq.writelines(lista_arq)
    print("arq.txt foi salvo")
    arq.close() # Sempre feixe o arquivo para que outras pessoas não tenha acesso.

def fn_r_arq(): #Aqui vai fazer a leitura
    arq = open("arq.txt", "r")
    lista_arq = []; ct_linha = 0
    print("Conteúdo do arquivo arq.txt")
    lista_arq = arq.readlines() # lista_arq recebe todo o arquivo para ler.
    for linha in lista_arq:
        ct_linha += 1
        print(str(ct_linha)+": "+linha, end="") # o + é para concatenar.
    arq.close()

def fn_a_arq(): # Função para escrever um texto de até 99 linhas.
    txt = open("txt.txt", "a")
    listar_txt = []
    print("Escreva um pequeno texto com POUCAS PALAVRAS até 99 frases")
    print("São POUCAS palavras, Digite até 100 palavras!")
    print("Para terminar o texto digite K")
    ct_linha1 = 0; linha1=""
    while linha1 != "K" and ct_linha1 <99: # a palavra tem que ser diferente de K e com menos de 99 linhas
        ct_linha1 += 1 # Vai contar as linhas +1
        print("Linhas " + str(ct_linha1), end=": ")
        linha1 = "01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
        while len(linha1) > 100:
            linha1=input()
            if len(linha1) > 100: print("Escreva mais!",end="")
        if linha1 != "K!": listar_txt.append(linha1 + "\n")
    print("salvando o arquivo arq.txt")
    txt.writelines(listar_txt)
    print("arq.txt foi salvo")
    txt.close() # Sempre feixe o arquivo para que outras pessoas não tenha acesso.

def fn_texto_r_arq():
    vogais="aeiouAEIOU"
    txt = open("txt.txt", "r")# Open abriou o arquivo txt em modo leitura.
    listar_txt = []
    ct_linha1=0
    print("O texto é: ")
    listar_txt = txt.readlines()# A lista vai receber todo o arquivo e vai ler todo o elemento da lista.
    for linha in listar_txt: # O for vai passar por todos os elementos da lista txt e passar esses elementos para "linha".
        ct_linha1 += 1 # Vai contar a linha em + uma unidade.
        ct_vogais = 0
        for letra in linha: # Vai contar as vogais
            #Se a letra esta dentro(in) das vogais vai contar as vogais.
            if letra in vogais: ct_vogais += 1
        print(str(ct_linha1)+". vogais"+str(ct_vogais)+ "  Frase: "+linha, end="") # o + é para concatenar.
    txt.close()





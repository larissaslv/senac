# Exibe os caracteres de A até Z em 8 cores para o texto combinadas com 8 cores para o fundo
def fn_exibe_cores():
    for cor_fundo in range(40, 48):  # Cores de fundo (40 a 47)
        for cor_texto in range(30, 38):  # Cores de texto (30 a 37)
            for caracter in range(65, 91):  # Caracteres de 'A' a 'Z'
                codigo_ansi = f"\033[{cor_texto};{cor_fundo}m{chr(caracter)}\033[0m"
                print(codigo_ansi, end=" ")
            print()  # Pula para a próxima linha após cada cor de texto
        print()  # Pula uma linha extra após cada cor de fundo
# Exibe o texto colorido
# Entradas
# - legenda das cores -> PRETO, VERMELHO, VERDE, AMARELO, AZUL, LILAS, AZULCLARO, CINZA
# - fundo: cor de fundo escrito em maiúscula de acordo com a legenda (string)
# - texto: cor do texto escrito em maiúscula de acordo com a legenda (string)
# - msg: mensagem a ser exibida na tela (string)
# - quebra: quebra de linha para a mensagem - 0(não quebra) 1(quebra) (int)
def fn_cor_texto(fundo, texto, msg, quebra):
    lista_cores = ["PRETO", "VERMELHO", "VERDE", "AMARELO", "AZUL", "LILAS", "AZULCLARO", "CINZA"]
    try:
        cor_fundo = lista_cores.index(fundo)
        cor_texto = lista_cores.index(texto)
    except:
        cor_fundo = 0
        cor_texto = 7
    cor_fundo += 40
    cor_texto += 30
    if quebra:
        print(f"\033[{cor_texto};{cor_fundo}m{msg}\033[0m")
    else:
        print(f"\033[{cor_texto};{cor_fundo}m{msg}\033[0m", end="")

# Define, via teclado, as cores de fundo e do texto e a mensagem a ser exibida
def fn_texto_cor():
    print("Texto colorido")
    print("Cores disponíveis")
    print("PRETO VERMELHO VERDE AMARELO AZUL LILAS AZULCLARO CINZA")
    cor_fundo = input("Cor de fundo: ")
    cor_texto = input("Cor do texto: ")
    mensagem  = input("Mensagem    : ")
    fn_cor_texto(cor_fundo, cor_texto, mensagem, 1)

import Consistencias
import Cores

# Exibe o mes do calendário
# Entradas
# - num_dias: numero de dias do mês [28 - 31] (int)
# - dia_sem_ini: numero do dia da semana que inicia o mês [0 - 6] (int)
# - num_mes: numero do mês para exibir o nome do mês [0 - 11] (int)
# Saídas
# - 6 ou coluna -1: número do dia da semana que o mês termina [0 - 6]
# Cores.fn_cor_texto(cor_fundo, cor_texto, mensagem, 1): exibe na cor desejada
def fn_matriz(num_dias, dia_sem_ini, num_mes, lista_dias):
    mes = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]
    conta = 0; ct_dia_sem = 0
    Cores.fn_cor_texto("PRETO", "VERMELHO", mes[num_mes] + " " * (28 - len(mes[num_mes])), 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", " D   S   T   Q   Q   S   S  ", 1)
    for linha in range(6):
        for coluna in range(7):
            if ct_dia_sem < dia_sem_ini:
                print(end=("    "))
                ct_dia_sem += 1
            else:
                conta += 1
                if conta <= num_dias:
                    if conta in lista_dias:
                        Cores.fn_cor_texto("PRETO", "LILAS", f"{conta:02d}" + "  ", 0)
                    else:
                        if coluna == 0: Cores.fn_cor_texto("PRETO", "VERDE", f"{conta:02d}" + "  ", 0)
                        else: Cores.fn_cor_texto("PRETO", "AZUL", f"{conta:02d}" + "  ", 0)
                else:
                    print()
                    if coluna == 0: return 6
                    else: return(coluna - 1)
        print()

# Exibe o calendário do mês definido pelo usuário
# Leitura via teclado
# - num_mes: número do mês para exibir o nome [1 - 12] (int)
# - num_dias: número de dias do mês [28 - 31] (int)
# - dia_sem_ini: número do dia da semana que inicia o mês [0 - 6] (int)
# - lista_dias: dias que se tem compromisso
def fn_calendario():
    num_dias = 0; dia_sem_ini = -1; num_mes = 0
    lista_sem = ["DOMINGO", "SEGUNDA", "TERÇA", "QUARTA", "QUINTA", "SEXTA", "SÁBADO"]
    print("Número do mês")
    while num_mes < 1 or num_mes > 12:
        num_mes = int(input("JAN:1 FEV:2 MAR:3 ABR:4 MAI:5 JUN:6 JUL:7 AGO:8 SET:9 OUT:10 NOV:11 DEZ:12 -> "))
    while num_dias < 28 or num_dias > 31:
        num_dias = int(input("Dias do mês entre 28 e 31: "))
    print("Número do dia da semana que inicia o mês")
    while dia_sem_ini < 0 or dia_sem_ini > 6:
        dia_sem_ini = int(input("DOM:0 SEG:1 TER:2 QUA:3 QUI:4 SEX:5 SAB:6 -> "))
    print("O mês terminou no(a): " + lista_sem[fn_matriz(num_dias, dia_sem_ini, num_mes - 1, [0])])

# Exibe o calendário com os meses do ano definido pelo usuário
# Leitura via teclado
# - ano: [1900 - 2100] (int)
def fn_ano():
    print("Calendário")
    print("Ano do calendário")
    ano = Consistencias.fn_consiste_int(1900, 2100, "Ano entre 1900 e 2100")
    bissexto = Consistencias.fn_verifica_bissexto(ano)
    sem = Consistencias.fn_verifica_inicio_ano(ano)
    for ct_mes in range(1, 13):
        if ct_mes in [1, 3, 5, 7, 8, 10, 12]: dias_mes = 31
        elif ct_mes == 2: dias_mes = 28 + bissexto
        else: dias_mes = 30
        sem_aux = fn_matriz(dias_mes, sem, ct_mes - 1, [0])
        if sem_aux == 6: sem = 0
        else: sem = sem_aux + 1

# Exibe o mes do ano especificado com os compromissos
# Entradas
# - ano: [1900 - 2100] (int)
# - mes: [1 - 12] (int)
# - lista_ano: lista com os anos de compromissos
# - lista_mes: lista com os meses de compromisso
# - lista_dia: lista com os dias de compromisso
# Saída
# - dias_mes: quantidade de dias do mês exibido
def fn_mostrames(ano, mes, lista_ano, lista_mes, lista_dia):
    lista_diasdomes = []
    for conta in range(len(lista_ano)):
        if lista_ano[conta] == ano and lista_mes[conta] == mes:
            lista_diasdomes.append(lista_dia[conta])
    dia_sem = Consistencias.fn_verifica_dia_sem(ano, mes, 1)
    if mes in [1, 3, 5, 7, 8, 10, 12]: dias_mes = 31
    elif mes == 2: dias_mes = 28 + Consistencias.fn_verifica_bissexto(ano)
    else: dias_mes = 30
    fn_matriz(dias_mes, dia_sem, mes - 1, lista_diasdomes)
    return dias_mes

def fn_evento():
    lista_ano = []; lista_mes = []; lista_dia = []; lista_evento = []
    try:
        arq = open("agenda.txt", "r")
        lista_arq = arq.readlines()
    except:
        arq = open("agenda.txt", "w")
        lista_arq = []
    for linha in lista_arq:
        lista_linha = linha.split("][")
        lista_ano.append(lista_linha[0])
        lista_mes.append(lista_linha[1])
        lista_dia.append(lista_linha[2])
        lista_evento.append(lista_linha[3])
    arq.close()
    print("Agende seu evento")
    opt = 1
    while opt == 1 or opt == 3:
        print("Digite o ano ...")
        ano = Consistencias.fn_consiste_int(1900, 2100, "...entre 1900 e 2100")
        print("JAN:1 FEV:2 MAR:3 ABR:4 MAI:5 JUN:6 JUL:7 AGO:8 SET:9 OUT:10 NOV:11 DEZ:12")
        print("Digite o número do mês ...")
        mes = Consistencias.fn_consiste_int(1, 12, "...entre 1 e 12")
        dias_mes = fn_mostrames(ano, mes, lista_ano, lista_mes, lista_dia)
        print("Digite o dia do mês ...")
        dia = Consistencias.fn_consiste_int(1, dias_mes, "...entre 1 e " + str(dias_mes))
        evento = input("Descreva o evento: ")
        print("1(Confirma e inicio) 2(Confirma e fim) 3(Não confirma e inicio) 4(Não confirma e fim)")
        print("Digite a opção...")
        opt = Consistencias.fn_consiste_int(1, 4, "...entre 1 e 4")
        if opt == 1 or opt == 2:
            lista_ano.append(ano)
            lista_mes.append(mes)
            lista_dia.append(dia)
            lista_evento.append(evento)
            Cores.fn_cor_texto("PRETO", "CINZA", "EVENTO CADASTRADO" + " " * 11, 1)
            dias_mes = fn_mostrames(ano, mes, lista_ano, lista_mes, lista_dia)
    lista_arq = []
    for ct_linha in range(len(lista_ano)):
        linha = str(lista_ano[ct_linha]) + "][" + str(lista_mes[ct_linha]) + "][" + str(lista_dia[ct_linha]) + "]["
        linha += lista_evento[ct_linha] + "][" + "\n"
        lista_arq.append(linha)
    arq = open("agenda.txt", "w")
    arq.writelines(lista_arq)
    arq.close()

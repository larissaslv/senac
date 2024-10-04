import Consistencias
import Cores

def fn_matriz(num_dias, dia_sem_ini, num_mes, lista_dias, ano):
    mes = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]
    conta = 0; ct_dia_sem = 0
    Cores.fn_cor_texto("PRETO", "VERMELHO", mes[num_mes] + " DE " + str(ano) + " " * (22 - len(mes[num_mes])), 1)
    Cores.fn_cor_texto("PRETO", "VERMELHO", "   D   S   T   Q   Q   S   S  ", 1)
    for linha in range(6):
        for coluna in range(7):
            if coluna == 0: Cores.fn_cor_texto("PRETO", "AZUL", "  ", 0)
            if ct_dia_sem < dia_sem_ini:
                Cores.fn_cor_texto("PRETO", "AZUL", "    ", 0)
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
                    Cores.fn_cor_texto("PRETO", "AZUL","    ", 0)
        print()

def fn_calendario():
    num_ano = Consistencias.fn_consiste_int(1900, 2100, "Ano entre 1900 e 2100")
    print("JAN:1 FEV:2 MAR:3 ABR:4 MAI:5 JUN:6 JUL:7 AGO:8 SET:9 OUT:10 NOV:11 DEZ:12")
    num_mes = Consistencias.fn_consiste_int(1, 12, "Número do mês entre 1 e 12")
    num_dias = Consistencias.fn_consiste_int(28, 31, "Dias do mês entre 28 e 31")
    print("DOM:0 SEG:1 TER:2 QUA:3 QUI:4 SEX:5 SAB:6")
    dia_sem_ini = Consistencias.fn_consiste_int(0, 6, "Dia da semana que inicia o mês entre 0 e 6")
    fn_matriz(num_dias, dia_sem_ini, num_mes - 1, [0], num_ano)

def fn_ano():
    print("Calendário")
    print("Ano do calendário")
    ano = Consistencias.fn_consiste_int(1900, 2100, "Ano entre 1900 e 2100")
    for mes in range(1, 13):
        dias_mes = fn_mostrames(ano, mes, [0], [0], [0])

def fn_mostrames(ano, mes, lista_ano, lista_mes, lista_dia):
    lista_diasdomes = []
    for conta in range(len(lista_ano)):
        if lista_ano[conta] == ano and lista_mes[conta] == mes:
            lista_diasdomes.append(lista_dia[conta])
    dia_sem = Consistencias.fn_verifica_dia_sem(ano, mes, 1)
    if mes in [1, 3, 5, 7, 8, 10, 12]: dias_mes = 31
    elif mes == 2: dias_mes = 28 + Consistencias.fn_verifica_bissexto(ano)
    else: dias_mes = 30
    fn_matriz(dias_mes, dia_sem, mes - 1, lista_diasdomes, ano)
    return dias_mes

def fn_mostraevento(ano, mes, lista_ano, lista_mes, lista_dia, lista_eventos):
    Cores.fn_cor_texto("PRETO", "LILAS","DIA  ", 0)
    Cores.fn_cor_texto("PRETO", "AMARELO", "EVENTO" + " " * 19, 1)
    nao_evento = 1
    for conta in range(len(lista_ano)):
        if lista_ano[conta] == ano and lista_mes[conta] == mes:
            nao_evento = 0
            Cores.fn_cor_texto("PRETO", "LILAS", f"{lista_dia[conta]:02d}" + ":  ", 0)
            Cores.fn_cor_texto("PRETO", "AMARELO", lista_eventos[conta], 1)
    if nao_evento == 1:
        Cores.fn_cor_texto("PRETO", "LILAS", "***  ", 0)
        Cores.fn_cor_texto("PRETO", "AMARELO", "Não há eventos para este mês", 1)

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
        lista_ano.append(int(lista_linha[0]))
        lista_mes.append(int(lista_linha[1]))
        lista_dia.append(int(lista_linha[2]))
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
        fn_mostraevento(ano, mes, lista_ano, lista_mes, lista_dia, lista_evento)
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

def fn_consultaevento():
    lista_ano = []; lista_mes = []; lista_dia = []; lista_evento = []
    try:
        arq = open("agenda.txt", "r")
        lista_arq = arq.readlines()
    except:
        arq = open("agenda.txt", "w")
        lista_arq = []
    for linha in lista_arq:
        lista_linha = linha.split("][")
        lista_ano.append(int(lista_linha[0]))
        lista_mes.append(int(lista_linha[1]))
        lista_dia.append(int(lista_linha[2]))
        lista_evento.append(lista_linha[3])
    arq.close()
    print("Consulte seu evento")
    opt = 1
    while opt == 1:
        print("Digite o ano ...")
        ano = Consistencias.fn_consiste_int(1900, 2100, "...entre 1900 e 2100")
        print("JAN:1 FEV:2 MAR:3 ABR:4 MAI:5 JUN:6 JUL:7 AGO:8 SET:9 OUT:10 NOV:11 DEZ:12")
        print("Digite o número do mês ...")
        mes = Consistencias.fn_consiste_int(1, 12, "...entre 1 e 12")
        dias_mes = fn_mostrames(ano, mes, lista_ano, lista_mes, lista_dia)
        fn_mostraevento(ano, mes, lista_ano, lista_mes, lista_dia, lista_evento)

        print("1(Nova conculta) 2(Termina)")
        print("Digite a opção...")
        opt = Consistencias.fn_consiste_int(1, 2, "...entre 1 e 2")

def fn_apaga_evento():
    lista_ano = []; lista_mes = []; lista_dia = []; lista_evento = []
    try:
        arq = open("agenda.txt", "r")
        lista_arq = arq.readlines()
    except:
        arq = open("agenda.txt", "w")
        lista_arq = []
    for linha in lista_arq:
        lista_linha = linha.split("][")
        lista_ano.append(int(lista_linha[0]))
        lista_mes.append(int(lista_linha[1]))
        lista_dia.append(int(lista_linha[2]))
        lista_evento.append(lista_linha[3])
    arq.close()
    print("Apague o seu evento")
    opt = 1
    while opt == 1:
        print("Digite o ano ...")
        ano = Consistencias.fn_consiste_int(1900, 2100, "...entre 1900 e 2100")
        print("JAN:1 FEV:2 MAR:3 ABR:4 MAI:5 JUN:6 JUL:7 AGO:8 SET:9 OUT:10 NOV:11 DEZ:12")
        print("Digite o número do mês ...")
        mes = Consistencias.fn_consiste_int(1, 12, "...entre 1 e 12")
        dias_mes = fn_mostrames(ano, mes, lista_ano, lista_mes, lista_dia)
        lista_dia_aux = []
        for ct_conta in range(len(lista_ano)):
            if ano == lista_ano[ct_conta] and mes == lista_mes[ct_conta]:
                lista_dia_aux.append(lista_dia[ct_conta])
        if len(lista_dia_aux) > 0:
            dia = 0
            while not (dia in lista_dia_aux):
                print("Digite o dia do mês ...")
                dia = Consistencias.fn_consiste_int\
                    (1, dias_mes, "...entre 1 e " + str(dias_mes))
                if not (dia in lista_dia_aux):
                    print("Digite apenas dias com eventos!")
            lista_evento_aux = []
            for ct_conta in range(len(lista_ano)):
                if ano == lista_ano[ct_conta] and \
                        mes == lista_mes[ct_conta] and \
                        dia == lista_dia[ct_conta]:
                    lista_evento_aux.append(lista_evento[ct_conta])
            for ct_conta in range(len(lista_evento_aux)):
                Cores.fn_cor_texto("PRETO", "LILAS", str(ct_conta + 1)+"  ", 0)
                Cores.fn_cor_texto("PRETO", "AMARELO", lista_evento_aux[ct_conta], 1)
            print("Digite o número do evento para apagar")
            del_evento = Consistencias.fn_consiste_int(1, ct_conta + 1, "Entre 1 e " + str(ct_conta + 1))
            del_linha_evento = -1
            for ct_conta in range(len(lista_ano)):
                if ano == lista_ano[ct_conta] and mes == lista_mes[ct_conta] and dia == lista_dia[ct_conta] and lista_evento_aux[del_evento -1] == lista_evento[ct_conta]:
                    del_linha_evento = ct_conta
            if del_linha_evento >= 0:
                del lista_ano[del_linha_evento]
                del lista_mes[del_linha_evento]
                del lista_dia[del_linha_evento]
                del lista_evento[del_linha_evento]

            lista_arq = []
            for ct_linha in range(len(lista_evento)):
                linha = str(lista_ano[ct_linha]) + "][" + str(lista_mes[ct_linha]) + "][" + str(lista_dia[ct_linha]) + "]["
                linha += lista_evento[ct_linha] + "][" + "\n"
                lista_arq.append(linha)
            arq = open("agenda.txt", "w")
            arq.writelines(lista_arq)
            arq.close()

        else:
            print("Não há eventos em " + str(mes) + "/" + str(ano))
        print("1(Nova conculta) 2(Termina)")
        print("Digite a opção...")
        opt = Consistencias.fn_consiste_int(1, 2, "...entre 1 e 2")

'''
       for ct_conta in range(len(lista_ano)):
                if ano == lista_ano[ct_conta] and \
                        mes == lista_mes[ct_conta] and \
                        dia == lista_dia[ct_conta]:
                    lista_evento_aux.append(lista_evento[ct_conta])
'''
'''

        for ct_conta in range(len(lista_evento_aux)): # Exibe os eventos do dia
            print(ct_conta + 1, lista_evento_aux[ct_conta])
'''






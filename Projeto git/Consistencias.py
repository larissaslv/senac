# Consiste número inteiro no intervalo
# Entradas
# - ini: inicio intervalo (int)
# - fim: fim intervalo (int)
# - msg: mensagem de texto (string)
# Saida
# - num: numero digitado no intervalo (int)
def fn_consiste_int(ini, fim, msg):
    num = fim + 1
    while num < ini or num > fim:
        try:
            num = int(input(msg + ": "))
        except:
            print("Valor digitado deve ser um número inteiro !")
            num = fim + 1
        if num < ini or num > fim:
            print("Valor digitado deve ser entre " + str(ini) + " e " + str(fim) + " !")
    return num

# Verifica se o  ano é bissexto
# Entrada
# - ano: ano, maior do que 0 a ser verificado (int)
# Saída
# - bissexto: 1(bissexto) 0(não bissexto) (int)
def fn_verifica_bissexto(ano):
    if ano % 400 == 0: bissexto = 1
    elif ano % 100 == 0: bissexto = 0
    elif ano % 4 == 0: bissexto = 1
    else: bissexto = 0
    if bissexto: print("O ano " + str(ano) + " é bissexto.")
    else: print("O ano " + str(ano) + " não é bissexto.")
    return bissexto

# Retorna o dia da semana que inicia o ano
# Entrada
# - ano: ano maior do que 0 a ser verificado (int)
# Saída
# - dia_ini: número do dia da semana que inicia o ano [0 - 6] (int)
def fn_verifica_inicio_ano(ano):
    ano_aux = ano - 1
    bis_aux = ano_aux // 4 - ano_aux // 100 + ano_aux // 400
    dia_ini = (1 + ano_aux + bis_aux + (31 * 11) // 12) % 7
    return dia_ini

# Retorna o dia da semana de um mês específico do ano definido
# Entradas
# - ano: ano definido [1900 - 2100] (int)
# - mes: mes selecionado do ano [1- 12] (int)
# - dia: dia do mes selecionado do mes [1 - 31] (int)
# Saida
# - dia_ini: númereo do dia da semana [0 - 6] (int)
def fn_verifica_dia_sem(ano, mes, dia):
    mes_aux = (14 - mes) // 12
    ano_aux = ano - mes_aux
    mes_res = mes + 12 * mes_aux - 2
    bis_aux = ano_aux // 4 - ano_aux // 100 + ano_aux // 400
    dia_ini = (dia + ano_aux + bis_aux + (31 * mes_res) // 12) % 7
    return dia_ini

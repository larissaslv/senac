def fn_ins_estado():
    lista_est_cod=[]; lista_est_nome=[]

    try:
        arq = open("estado.txt", "r")
        lista_arq= arq.readlines()
    except:
        arq = open("estado.txt", "w")
        lista_arq = []
    for linha in lista_arq:
        lista_linha = linha.split("][")
        lista_est_cod.append(lista_linha[0])
        lista_est_nome.append(lista_linha[1])
    arq.close()
    est_cod = "" # est_cod recebe vazio e vai forçar entrar no while para tratamento de dados.
    while len(est_cod) != 2:
        est_cod = input("Digite o código do estado: ")
        if len(est_cod) != 2: # Se o código for diferente de 2 caracteres, vai fazer o tratamento de erro.
            print("Erro! O código deve ter DOIS Caracteres! ")
        if est_cod in lista_est_cod:
            print("Essen código já existe! ")
            est_cod=""
    est_nome = input("Nome do estado: ")
    lista_est_cod.append(est_cod)
    lista_est_nome.append(est_nome)
    print(lista_est_cod, lista_est_nome)
    lista_arq = []
    for ct_linha in range(len(lista_est_cod)):
        linha = lista_est_cod[ct_linha] + "][" + lista_est_nome[ct_linha] + "][" + "\n"
        lista_arq.append(linha)
    print(lista_arq)
    arq = open("estado.txt", "w")
    arq.writelines(lista_arq)
    arq.close()

def fn_consulta_estado():
    try:
        arq = open("estado.txt", "r")
        lista_arq = arq.readlines()
        print("try")
    except:
        arq = open("estado.txt", "w")
        lista_arq = []
        print("except")
    for linha in lista_arq:
        print(linha)










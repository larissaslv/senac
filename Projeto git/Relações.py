def fn_le_estado():
    lista_est_cod = []; lista_est_nome = []
    try:
        arq = open("estados.txt", "r")
        lista_arq = arq.readlines()
    except:
        arq = open("estados.txt", "w")
        lista_arq = []
    for linha in lista_arq:
        lista_linha = linha.split("][")
        lista_est_cod.append(lista_linha[0])
        lista_est_nome.append(lista_linha[1])
    arq.close()
    return lista_est_cod, lista_est_nome

def fn_grava_estado(lista_est_cod, lista_est_nome):
    lista_arq = []
    for ct_linha in range(len(lista_est_cod)):
        linha = lista_est_cod[ct_linha] + "][" + lista_est_nome[ct_linha] + "][" + "\n"
        lista_arq.append(linha)
    arq = open("estados.txt", "w")
    arq.writelines(lista_arq)
    arq.close()

def fn_ins_estado():
    lista_est_cod, lista_est_nome = fn_le_estado()
    print("Insere um estado")
    est_cod = ""
    while len(est_cod) != 2:
     est_cod = input("Código do estado:")
     if len(est_cod) != 2:
         print("ERRO - Código do estado deve ter somente 2 caracteres !")
     if est_cod in lista_est_cod:
         print("ERRO - Esse código já existe !")
         est_cod = ""
    est_nome = input("Nome do estado: ")
    lista_est_cod.append(est_cod)
    lista_est_nome.append(est_nome)
    fn_grava_estado(lista_est_cod, lista_est_nome)

def fn_con_estado():
    lista_est_cod, lista_est_nome = fn_le_estado()
    print("Consulta estados - listagem")
    print("==", "=" * 40)
    if len(lista_est_cod) > 0:
        for ct_conta in range(len(lista_est_cod)):
            print(lista_est_cod[ct_conta], lista_est_nome[ct_conta])
    else: print("   Nenhum estado foi cadastrado!")
    print("==", "=" * 40)

def fn_del_estado():
    lista_est_cod, lista_est_nome = fn_le_estado()
    print("Apague o estado ")
    est_cod = ""; interrompe = 0
    while len(est_cod) != 2 and interrompe == 0:
      est_cod = input("Código do estado (** retorna ao menu):")
      if len(est_cod) != 2:
          print("ERRO - Código do estado deve ter somente 2 caracteres !")
      elif not (est_cod in lista_est_cod):
            print("ERRO - Esse código não existe !")
      if est_cod == "**":
          interrompe = 1
          print("Retorna ao menu")
    if interrompe == 0:
        est_nome = input("Nome do estado: ")
    del_est = lista_est_cod.index(est_cod)
    print("Apagando " + lista_est_cod[del_est], end=" ")
    print(lista_est_nome[del_est])
    del lista_est_cod[del_est]
    del lista_est_nome[del_est]
        # faz a rotina para apagar o codi e o nome nas listas
    fn_grava_estado(lista_est_cod, lista_est_nome)


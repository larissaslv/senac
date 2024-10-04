import Fatorial
import Arquivos
import Triangulo
import jogos
import Cores
import Agenda
import Relações
def menu_principal():
    print(''' 
Menu Principal

1. Menu Fatorial
2. Menu Triangulo
3. Menu Arquivo
4. jogo
5. Cores
6. Agenda 
7. Relações
0. Termina a brincadeira
''')
    '''
     pr=input("Digite uma opção: ")
    if pr==1:
        print(fn_menu_fatorial)
    '''



def fn_menu_fatorial():
    # opções do menu
    print("Menu:")
    print("1. Fatorial com For")
    print("2. Fatorial com While")
    print("3. Fatorial com For reverso")
    print("4. Fatorial com While reverso")
    print("0. Para voltar pro menu principal ")
def fn_menu_triangulo():
    print("1. Verifica os lados de um triangulo")
    print("0. Para voltar pro menu principal ")
def fn_menu_arquivo():
    print("1. Cria, cadastra o conteúdo e salva o arquivo arq.txt")
    print("2. Lê e exibe o conteúdo do arquivo arq.txt")
    print("3. Escrever texto")
    print("4. Ler o texto")
    print("0. Para voltar pro menu principal ")

def fn_jogo():
    print("1. Gera e exibe os números da MegaSena: ")
    print("2. Grava em megasena.txt os numeros gerados")
    print("3. Lê de megasena.txt os números e exibe na forma de lista")
    print("0. Para voltar pro menu principal ")

def fn_menu_cores():
    print("Menu Cores")
    print("1. Gera uma paleta de 8 cores")
    print("2. Exibe texto colorido")
    print("0. Volta para o Menu Principal")

def fn_menu_agenda():
    print("Menu Agenda")
    print("1. Calendário")
    print("2. Calendário do ano")
    print ("3. Eventos")
    print("0. Volta para o Menu Principal")
def fn_sub_agenda():
    print("1. Inserir")
    print("2. Listar")
    print("3. Consultar")
    print("4. Apagar")
    print("0. Volta para o Menu Principal")

def fn_relacoes():
    print("1. Estado")
    print("2. Cidade")
    print("3. Bairro")
    print("0. Volta para o Menu Principal")
def fn_estado():
    print("1. Inserir: ")
    print("2. Consultar: ")
    print("3. Apagar: ")
    print("0. Volta para o Menu Principal")
def fn_cidade():
    print("1. Inserir: ")
    print("2. Consultar: ")
    print("3. Apagar: ")
    print("0. Volta para o Menu Principal")
def fn_bairro():
    print("1. Inserir: ")
    print("2. Consultar: ")
    print("3. Apagar: ")
    print("0. Volta para o Menu Principal")
while True:
    menu_principal()
    opcao = input("Escolha uma opção: ")
    # seleciona a função de acordo com a opção
    if opcao == '1':
        while True:
            fn_menu_fatorial()
            opcao1 = input("Escolha uma opção: ")
            if opcao1 == '1': Fatorial.FnFor()
            elif opcao1 == '2': Fatorial.FnWhile()
            elif opcao1 == '3': Fatorial.FnForReverso()
            elif opcao1 == '4': Fatorial.FnWhileReverso()
            elif opcao1 == '0': break

    elif opcao == '2':
        while True:
            fn_menu_triangulo()
            opcao2 = input("escolha uma opção: ")
            if opcao2== '1': Triangulo.fn_tri_verifica()
            elif opcao2 == '0': break
    elif opcao == '3':
        while True:
            fn_menu_arquivo()
            opcao3 = input("Digite uma opção: ")
            if opcao3 == '1':Arquivos.fn_w_arq() # Faz a escrita dos arquivos
            elif opcao3 == '2': Arquivos.fn_r_arq() # Faz a leitura dos arquivos.
            elif opcao3 == '3': Arquivos.fn_a_arq()
            elif opcao3 == '4': Arquivos.fn_texto_r_arq()
            elif opcao3 == '0': break
        print("Kabô !!!")
        break

    elif opcao == '4':
        while True:
            fn_jogo()
            opcao4 = input("Digite uma opção: ")
            if opcao4 == '1': jogos.geranum()
            elif opcao4 == '2': jogos.fn_arqmega()
            elif opcao4 == '3': jogos.fn_listamega()
            elif opcao4 == '4': break
    elif opcao == '5':
        while True:
            fn_menu_cores()
            opcao2 = input("Escolha uma opção: ")
            if opcao2 == '1':   Cores.fn_exibe_cores()
            elif opcao2 == '2': Cores.fn_texto_cor()
            elif opcao2 == '0': break
    elif opcao == '6':
        while True:
            fn_menu_agenda()
            opcao6 = input("Escolha uma opção: ")
            if opcao6 == '1':   Agenda.fn_calendario()
            elif opcao6 == '2': Agenda.fn_ano()
            elif opcao6 == '3':
                fn_sub_agenda()
            opcao = input("Escolha uma opção: ")
            if opcao == '1': Agenda.fn_evento()
            elif opcao == '2': Agenda.fn_consultaevento()
            elif opcao == '3': Agenda.fn_consultaevento()
            elif opcao == '4': Agenda.fn_apaga_evento()
            elif opcao == '0': break
    elif opcao == '7':
        while True:
            fn_relacoes()
            opcao7=input("Escolha uma opção: ")
            if opcao7 == '1':
                while True:
                    fn_bairro()
                    opcao=input("Escolha uma opção: ")
                    if opcao=='1': Relações.fn_ins_estado()
                    elif opcao == '2': Relações.fn_con_estado()
                    elif opcao == '3': Relações.fn_del_estado()
            elif opcao7 == '0': break
    else:
        print("Opção inválida!")


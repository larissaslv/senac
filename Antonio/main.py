
import fatorial
import triangulo
import Arquivo
def fn_menu():
    # opções do menu
    print("Menu:")
    print("1. Fatorial com For")
    print("2. Fatorial com While")
    print("3. Fatorial com For reverso")
    print("4. Fatorial com While reverso")
    print("5. Verifica os lados de um triangulo")
    print("6. Cria, cadastra o conteúdo e salva o arquivo arq.txt")
    print("7. Lê e exibe o conteúdo do arquivo arq.txt")
    print("8. Cadastra um texto")
    print("9. Lê o texto e conta as vogais de cada linha")
    print("0. Termina a brincadeira")

while True:
    fn_menu()
    opcao = input("Escolha uma opção: ")
    # seleciona a função de acordo com a opção
    if opcao == '1':   fatorial.FnFor()
    elif opcao == '2': fatorial.FnWhile()
    elif opcao == '3': fatorial.FnForReverso()
    elif opcao == '4': fatorial.FnWhileReverso()
    elif opcao == '5': triangulo.fn_tri_verifica()
    elif opcao == '6': Arquivo.fn_w_arq()
    elif opcao == '7': Arquivo.fn_r_arq()
    elif opcao == '8': Arquivo.fn_texto_a_arq()
    elif opcao == '9': Arquivo.fn_texto_r_arq()
    elif opcao == '0':
        print("Kabô !!!")
        break
    else:
        print("Opção inválida!")





